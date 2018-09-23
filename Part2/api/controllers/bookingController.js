'use strict';


var mongoose = require('mongoose'),
  Booking = mongoose.model('Available Bookings');

exports.list_all_bookings = function(req, res) {
  Booking.find({}, function(err, booking) {
    if (err)
      res.send(err);
    res.json(booking);
  });
};




exports.create_a_booking = function(req, res) {
  var new_booking = new Booking(req.body);
  new_booking.save(function(err, booking) {
    if (err)
      res.send(err);
    res.json(booking);
  });
};


exports.read_a_booking = function(req, res) {
  Booking.find({name: req.params.supplier}, function(err, booking) {
    if (err)
      res.send(err);
    res.json(booking);
  });
};


exports.update_a_booking = function(req, res) {
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
