/*!
    * Start Bootstrap - Agency v6.0.3 (https://startbootstrap.com/theme/agency)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-agency/blob/master/LICENSE)
    */
    (function ($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (
            location.pathname.replace(/^\//, "") ==
                this.pathname.replace(/^\//, "") &&
            location.hostname == this.hostname
        ) {
            var target = $(this.hash);
            target = target.length
                ? target
                : $("[name=" + this.hash.slice(1) + "]");
            if (target.length) {
                $("html, body").animate(
                    {
                        scrollTop: target.offset().top - 72,
                    },
                    1000,
                    "easeInOutExpo"
                );
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $(".js-scroll-trigger").click(function () {
        $(".navbar-collapse").collapse("hide");
    });
    
    // Activate scrollspy to add active class to navbar items on scroll
    $("body").scrollspy({
        target: "#mainNav",
        offset: 74,
    });
    
    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#mainNav").offset().top > 100) {
            $("#mainNav").addClass("navbar-shrink");
        } else {
            $("#mainNav").removeClass("navbar-shrink");
        }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);
})(jQuery); // End of use strict


function reference(){
    location.href = "#gene";
}

var btn_val = []
function get_value(obj) {
    btn_val.push(obj)
    if (btn_val.length === 2) {
        if (btn_val[0] === btn_val[1]){
            alert("You can't choose " + btn_val[0] + " and " + btn_val[1] + ".");
            btn_val = [];
        }
        else {
            if (btn_val[0] !== "I2959" & btn_val[0] !== "LAP"){
                tmp = btn_val[0];
                btn_val[0] = btn_val[1];
                btn_val[1] = tmp;
            }
            alert("You choose " + btn_val[0] + " and " + btn_val[1] + ". \nThe HTML file is too large, please wait patiently.");
            document.getElementById("resultName").innerHTML = "Model result"
            if (btn_val[0] === "I2959"){
                document.getElementById("htmlfile").src = "/static/assets/model/mechanical/" + btn_val[1] + "_Predict_Model_" + btn_val[0] + ".html"
            }
            else if (btn_val[0] === "LAP"){
                document.getElementById("htmlfile").src = "/static/assets/model/mechanical/" + btn_val[1] + "_Predict_Model_w_EXP_" + btn_val[0] + ".html"
            }
            document.getElementById("result_navigator").style.display = 'block';
            document.getElementById("result").style.display = 'block';
            window.location.href = "#result"
            btn_val = [];
            $("#tensile").attr('disabled', true);
            $("#youngs").attr('disabled', true);
        }
    }
    else if (btn_val.length === 1) {
        $("#tensile").removeAttr('disabled');
        $("#youngs").removeAttr('disabled');
    }       
}
function block_redirect(){
    var r = confirm("Are you sure to logout?");
    if (r === true) {
        window.location.href = "/welcome/";
    }
}
function showpicture(){
    var d = document.getElementById("table_id");
    for(var i=0;i<d.rows.length;i++){
        for(var j=0;j<d.rows[i].cells.length;j++){
            if (j==6){
                var al = d.rows[i].cells[j].children[0].innerHTML;
            }  
        }
    }
}

window.onload = function(){
    //experiment.html
    var checkstate = 0;
    var checkstate2 = 0;
    var checksimstate = 0;
    var checksimstate2 = 0;
    $('input:radio[name="cell_diff_tissue"]').attr('disabled', true);
    
    $('input:radio[name="mechanical"]').click(function (){ 
        if (checkstate === true){
            this.checked = false;
        }
        else{
            this.checked = true;
        }
        if (this.checked) {
            $('input:radio[name="cell_diff_expression"]').attr('disabled', true);
            $('input:radio[name="cell_diff_tissue"]').attr('disabled', true);
        }
        else {
            $('input:radio[name="cell_diff_expression"]').attr('disabled', false);
            $('input:radio[name="cell_diff_tissue"]').attr('disabled', true);
        }
        checkstate = this.checked;
    })
    
    $('input:radio[name="cell_diff_expression"]').click(function() {
        var exp = this.value;
        if (exp === checkstate2){
            this.checked = false;
            exp = this.checked;
        }
        if (exp === "score") {
            $('input:radio[name="mechanical"]').attr('disabled', true);
            $('input:radio[name="cell_diff_tissue"]').attr('disabled', true);
        }
        else if (exp === "CtValue") {
            $('input:radio[name="mechanical"]').attr('disabled', true);
            $('input:radio[name="cell_diff_tissue"]').attr('disabled', false);
        }
        else if (exp === "FoldChange") {
            $('input:radio[name="mechanical"]').attr('disabled', true);
            $('input:radio[name="cell_diff_tissue"]').attr('disabled', false);
        }
        else {
            $('input:radio[name="mechanical"]').attr('disabled', false);
            $('input:radio[name="cell_diff_tissue"]').attr('disabled', true);
        }
        checkstate2 = exp
    })

    $('input:radio[name="simparameter"]').click(function() {
        if (checksimstate === true) {
            this.checked = false;
            $('input:radio[name="simpicture"]').attr('disabled', false);
        }
        else{
            this.checked = true;
            $('input:radio[name="simpicture"]').attr('disabled', true);
        }
        checksimstate = this.checked;
    })

    $('input:radio[name="simpicture"]').click(function () {
        if (checksimstate2 === true) {
            this.checked = false;
            $('input:radio[name="simparameter"]').attr('disabled', false);
            document.getElementById("simchoose").style.display = 'none';
        }
        else {
            this.checked = true;
            $('input:radio[name="simparameter"]').attr('disabled', true);
            document.getElementById("simchoose").style.display = 'block';
        }
        checksimstate2 = this.checked;
    })
}

