'use strict';


var mongoose = require('mongoose'),
  Booking = mongoose.model('Available Bookings');

exports.list_all_avail_bookings = function(req, res) {
  Booking.find({$and: [{pickupLat: req.params.pickupLat}, {pickupLong: req.params.pickupLong}, {dropoffLat: req.param.dropoffLat}, {dropoffLong: req.param.dropoffLong}]}, function(err, booking) {
    if (err)
      res.send(err);
    res.json(booking);
  });
};


exports.create_a_booking = function(req, res) {
  var new_booking = new Booking(req.body);
  new_booking.save({}, function(err, booking) {
    if (err)
      res.send(err);
    res.json(booking);
  });
};


exports.list_avail_booking_one_supplier = function(req, res) {
  Booking.find({$and: [{name: req.params.supplier}, {pickupLat: req.params.pickupLat}, {pickupLong: req.params.pickupLong}, {dropoffLat: req.params.dropoffLat}, {dropoffLong: req.params.dropoffLong}]}, function(err, booking) {
    if (err)
      res.send(err);
    res.json(booking);
  });
};


exports.update_an_avail_booking = function(req, res) {
  Booking.findOneAndUpdate({_id: req.params.supplier}, req.body, {new: true}, function(err, booking) {
    if (err)
      res.send(err);
    res.json(booking);
  });
};


exports.delete_a_booking = function(req, res) {


  Booking.remove({
    _id: req.params.bookingID
  }, function(err, booking) {
    if (err)
      res.send(err);
    res.json({ message: 'Booking successfully deleted' });
  });
};
