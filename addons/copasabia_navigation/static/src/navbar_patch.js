/** @odoo-module **/

import { NavBar } from "@web/webclient/navbar/navbar";
import { patch } from "@web/core/utils/patch";

patch(NavBar.prototype, {
    goToCopasabia() {
        window.location.href = 'http://localhost:8080';
    },
});
