// This is the scss entry file
import "../styles/index.scss";

// Load @hotwired/turbo
import * as Turbo from "@hotwired/turbo";

// Load @hotwired/stimulus & @hotwired/stimulus-webpack-helpers
import { Application } from "@hotwired/stimulus";
import { definitionsFromContext } from "@hotwired/stimulus-webpack-helpers";

// Initialize Stimulus through Webpack Helpers.
// Will automatically identify controllers in the controllers/
// directory. 

// If your controller file is named…	       its identifier will be…
//   clipboard_controller.js	                 clipboard
//   date_picker_controller.js	               date-picker
//   users/list_item_controller.js	           users--list-item
//   local-time-controller.js	                 local-time


window.Stimulus = Application.start();
const context = require.context("./controllers", true, /\.js$/);
Stimulus.load(definitionsFromContext(context));