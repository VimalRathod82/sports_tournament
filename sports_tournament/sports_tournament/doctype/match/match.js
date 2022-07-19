// Copyright (c) 2019, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Match', {
	// refresh: function(frm) {
	setup: function(frm) {
		frm.set_query("sport_game_name", function() {
			return {
				filters: {
					"parent": frm.doc.tournament_name,
				}
			};
			
		});
		frm.set_query("team_one", function() {
			return {
				filters: {
					tournament_name: frm.doc.tournament_name,
					sport_game: frm.doc.sport_game_name,
					sport_group_name: frm.doc.sport_group_name,
					name: ["not in",[frm.doc.team_two, frm.doc.ref_team_name]],
				}
			};
			
		});
		frm.set_query("team_two", function() {
			return {
				filters: {
					tournament_name: frm.doc.tournament_name,
					sport_game: frm.doc.sport_game_name,
					sport_group_name: frm.doc.sport_group_name,
					name: ["not in",[frm.doc.team_one, frm.doc.ref_team_name]],
				}
			};
		});
		frm.set_query("ref_team_name", function() {
			return {
				filters: {
					tournament_name: frm.doc.tournament_name,
					sport_game: frm.doc.sport_game_name,
					name: ["not in",[frm.doc.team_one, frm.doc.team_two]],
				}
			};
		});

		frm.set_query('team_name', 'match_awards', function(doc, cdt, cdn) {
			var d  = locals[cdt][cdn];
			return {
				"filters": {
					"name": ["in", [frm.doc.team_one, frm.doc.team_two]],
				}
			};
		});
		frm.set_query('player', 'match_awards', function(doc, cdt, cdn) {
			var d  = locals[cdt][cdn];
			return {
				"filters": {
					"parent": d.team_name,
				}
			};
		});
	},
	team_one: function(frm) {
		if (!frm.doc.team_one){
			frm.set_value("team_1_name", "");
		};
	},
	team_two: function(frm) {
		if (!frm.doc.team_two){
			frm.set_value("team_2_name", "");
		};
	},
	ref_team_name: function(frm) {
		if (!frm.doc.ref_team_name){
			frm.set_value("ref_team_name_name", "");
		};
	},
	sport_game_name: function(frm) {
		if (!frm.doc.sport_game_name){
			frm.set_value("sport_game_name1", "");
		};
	},
	team_one: function(frm) {
		populate_game_team_for_scores(frm, "Team 1 Name")
	},
	team_two: function(frm) {
		populate_game_team_for_scores(frm, "Team 2 Name")
	},
	no_of_games: function(frm) {
		populate_game_team_for_scores(frm, "Number of Games")
	},
});

function populate_game_team_for_scores(frm, field_changed){
	var i;
	// if (frm.doc.match_games) {
		// frappe.throw(__("The game scores are already entered. Please delete the scores before changing the {0} ", field_changed))
	// }
	if (frm.doc.no_of_games || frm.doc.team_one || frm.doc.team_two) {
		frm.clear_table("match_games");
		for (i = 0; i < frm.doc.no_of_games; i++) {
			// r.message.pump_meter_reading.forEach(d => {
			var child = frm.add_child("match_games");
			frappe.model.set_value(child.doctype, child.name, "game_no", i+1)
			frappe.model.set_value(child.doctype, child.name, "team_name", frm.doc.team_1_name)
			child = frm.add_child("match_games");
			frappe.model.set_value(child.doctype, child.name, "game_no", i+1)
			frappe.model.set_value(child.doctype, child.name, "team_name", frm.doc.team_2_name)
			// });
			refresh_field("match_games")
		}
	}
}
