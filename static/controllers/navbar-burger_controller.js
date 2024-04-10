import { Controller } from 'https://cdn.skypack.dev/@hotwired/stimulus';

export default class extends Controller {
    static targets = [ 'burger', 'menu' ]

    toggle() {
        this.burgerTarget.classList.toggle('is-active')
        this.menuTarget.classList.toggle('is-active');
    }
}