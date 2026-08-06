const express=require("express");
const router = express.Router();
const wrapAsync=require("../utils/wrapAsync.js");
const Listing = require("../models/listing.js");
const passport = require("passport");
const {isLoggedIn , isOwner , validateListing }=require("../middleware.js");
const listingcollrollers = require("../controllers/listings.js");
const { render } = require("ejs");
const multer  = require('multer');
const {storage} = require("../cloudConfig.js");
const upload = multer({ storage });


router
    .route("/")
    .get(wrapAsync(listingcollrollers.index))
    .post(
        isLoggedIn,
        upload.single('listing[image]'),
        validateListing,
        wrapAsync(listingcollrollers.createListing)
);
     
// New Route
 router.get("/new",isLoggedIn,listingcollrollers.renderNewForm);


router
   .route("/:id")
   .get(wrapAsync (listingcollrollers.showListing))
   .put(
    isLoggedIn, 
    upload.single('listing[image]'),
    isOwner,
    validateListing,
    wrapAsync(listingcollrollers.updateListing))
    .delete(
    isLoggedIn,
    isOwner, 
    wrapAsync(listingcollrollers.destroyListing )
);


//Edit Route
router.get(
    "/:id/edit",
    isLoggedIn ,
    isOwner,
    wrapAsync(listingcollrollers.renderEditeForm));

module.exports = router;