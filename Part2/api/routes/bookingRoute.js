'use strict';
module.exports = function(app) {
  var bookingList = require('../controllers/bookingController');

  //gives back all the car types from all the suppliers
  //unique key: latitude and longitudes of pickup and dropoff locations
  app.route('/allSuppliers')
    .get(bookingList.list_all_bookings)
    .post(bookingList.create_a_booking);


  app.route('/:supplier')
    .get(bookingList.read_a_booking)
    .post(bookingList.create_a_booking)
    .put(bookingList.update_a_booking)

  app.route('/:supplier/:bookingID')
    .delete(bookingList.delete_a_booking);







};
