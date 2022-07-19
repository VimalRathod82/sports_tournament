// Copyright (c) 2019, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sport Team', {
	// refresh: function(frm) {
	setup: function(frm) {
		frm.set_query("sport_game", function() {
			return {
				filters: {
					parent: frm.doc.tournament_name
				}
			};
		});
	},
	sport_game: function(frm) {
		if (!frm.doc.sport_game){
			frm.set_value("sports_game_name", "");
		};
	},
	// }
});
