'use strict';
var mongoose = require('mongoose');
var Schema = mongoose.Schema;


var BookingsSchema = new Schema({
  name: {
    type: String,
    required: 'Kindly enter the name of the supplier'
  },
  pickupLat: {
    type: String,
    required: 'Please enter the pickup latitude'
  },

  pickupLong: {
    type: String,
    required: 'Please enter the pickup longitude'
  },

  dropoffLat: {
    type: String,
    required: 'Please enter the dropoff latitude'
    },

  dropoffLong: {
    type: String,
    required: 'Please enter the dropoff longitude'
  },

  car_type_STANDARD_price: {
      type: String,
      default: "Not Available"
  },

  car_type_EXECUTIVE_price: {
      type: String,
      default: "Not Available"
  },

  car_type_LUXURY_price: {
      type: String,
      default: "Not Available"

  },

  car_type_PEOPLE_CARRIER_price: {
      type: String,
      default: "Not Available"
  },

  car_type_LUXURY_PEOPLE_CARRIER_price: {
      type: String,
      default: "Not Available"
  },

  car_type_MINIBUS_price: {
      type: String,
      default: "Not Available"
  }



});

module.exports = mongoose.model('Available Bookings', BookingsSchema);
