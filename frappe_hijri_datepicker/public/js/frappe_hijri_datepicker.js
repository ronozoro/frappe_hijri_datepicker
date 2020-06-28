frappe.ui.form.ControlDate = frappe.ui.form.ControlDate.extend({
    make_input: function () {
        var self = this;
        this.$input_extra_date = $("<" + this.html_element + ">")
            .attr("type", this.input_type)
            .attr("autocomplete", "off")
            .addClass("input-with-feedback form-control")
            .prependTo(this.input_area);
        this._super();
        function convert_to_hijri(date) {
            console.log(date)
            if (date.length === 0) {
                return false
            }
            var jd = $.calendars.instance('islamic').toJD(parseInt(date[0].year()), parseInt(date[0].month()), parseInt(date[0].day()));
            var date = $.calendars.instance('gregorian').fromJD(jd);
            var date_value = new Date(parseInt(date.year()), parseInt(date.month()) - 1, parseInt(date.day()));
            self.$input.val(self.format_for_input(date_value));
        }

        $(self.$input_extra_date).calendarsPicker({
            calendar: $.calendars.instance('islamic', 'ar'),
            onSelect: convert_to_hijri,
            showOnFocus: true,
        });
    },
    kuwaiticalendar: function (adjust) {
        if (adjust) {
            var today = new Date(moment(adjust).locale('en').format("YYYY-MM-DD"));
            var day = today.getDate();
            var month = today.getMonth() + 1;
            var year = today.getFullYear();
            var calendar = $.calendars.instance('gregorian', 'ar');
            var hijri_calendar = $.calendars.instance('islamic', 'ar');
            var jd = calendar.toJD(year, month, day);
            var date = hijri_calendar.fromJD(jd);
            var res = hijri_calendar.formatDate('yyyy-mm-dd', date.add(0, 'd'));
            return [res, ''];
        } else {
            return adjust;
        }

    },
    set_input: function (value) {
        this._super(value);
        if (value) {
            var h_value = this.kuwaiticalendar(value);
            $(this.$input_extra_date).val(h_value[0]);
        }

    },

})