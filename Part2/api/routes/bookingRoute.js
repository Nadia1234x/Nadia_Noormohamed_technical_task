'use strict';
module.exports = function(app) {
  var bookingList = require('../controllers/bookingController');

  app.route('/:supplier/:pickupLat/:pickupLong/:dropoffLat/:dropoffLong')
  //returns a booking from a particular supplier given the pickup and dropoff
  //locations
    .get(bookingList.list_avail_booking_one_supplier)
    .put(bookingList.update_an_avail_booking)

  //Used postman (google chrome extension) to add the available bookings into
  //the database
  app.route('/add_availability')
    .post(bookingList.create_a_booking)

  //delete a booking that is not available for some reason anymore.
  app.route('/:bookingID')
    .delete(bookingList.delete_a_booking);







};
