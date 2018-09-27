$(function() {
    $('#Add').click(function() {
        $.ajax({
            url: "/add",
            method: "POST",
            data: $('form').serialize(),
            success: function(d) {
                if (d['error']) {
                    $('#error').html(d['error']);
                    $('#result').html('');
                }
                else {
                    $('#result').html(d['n1'] + " + " + d['n2'] + " = " + d['result']);
                    $('#error').html('');
                }
            }
        });
    });

    $('#Subtract').click(function() {
        $.ajax({
            url: "/subtract",
            method: "POST",
            data: $('form').serialize(),
            success: function(d) {
                if (d['error']) {
                    $('#error').html(d['error']);
                    $('#result').html('');
                }
                else {
                    $('#result').html(d['n1'] + " - " + d['n2'] + " = " + d['result']);
                    $('#error').html('');
                }
            }
        });
    });

    $('#Divide').click(function() {
        $.ajax({
            url: "/divide",
            method: "POST",
            data: $('form').serialize(),
            success: function(d) {
                if (d['error']) {
                    $('#error').html(d['error']);
                    $('#result').html('');
                }
                else {
                    $('#result').html(d['n1'] + " / " + d['n2'] + " = " + d['result']);                    $('#error').html('');
                }
            }
        });
    });

    $('#Multiply').click(function() {
        $.ajax({
            url: "/multiply",
            method: "POST",
            data: $('form').serialize(),
            success: function(d) {
                if (d['error']) {
                    $('#error').html(d['error']);
                    $('#result').html('');
                }
                else {
                    $('#result').html(d['n1'] + " * " + d['n2'] + " = " + d['result']);                    $('#error').html('');
                }
            }
        });
    });
})