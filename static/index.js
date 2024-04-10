
import { Application } from 'https://cdn.skypack.dev/@hotwired/stimulus';
import NavbarBurgerController from './controllers/navbar-burger_controller.js';
// import * as Turbo from 'https://cdn.skypack.dev/@hotwired/turbo';



window.Stimulus = Application.start();
Stimulus.register("navbar-burger", NavbarBurgerController)

// @hotwired/Stimulus usage:


// If your controller file is named…	its identifier will be…
//  clipboard_controller.js	             clipboard
//  date_picker_controller.js	         date-picker
//  users/list_item_controller.js	     users--list-item
//  local-time-controller.js	         local-time

// import HelloController from "static/controllers/hello_controller"
// import ClipboardController from "static/controllers/clipboard_controller"

// window.Stimulus = Application.start();
// Stimulus.register("hello", HelloController)
// Stimulus.register("clipboard", ClipboardController)


