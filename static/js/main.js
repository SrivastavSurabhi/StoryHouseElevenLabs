$(".menubtn").click(function() {
    $(".sidebar").toggleClass("fullsidebar");
    $(".wrapper").toggleClass("lesswraper");
});

$(".closesidebar").click(function() {
    $(".sidebar").removeClass("fullsidebar");
    $(".wrapper").removeClass("lesswraper");
});



$(".hidebox").click(function() {
    $(this).parents('.uploading-box').hide();
    $('.sucess-box').show();
});
$('.reloadpage').click(function() {
    location.reload();
});


// // checkeach
// $('.checkboxes').change(function() {
//     var checkedNum = $('input.checkboxes:checked').length;
//     if (checkedNum == 0) {
//         $('.generate').attr('disabled', 'disabled');
//     } else if (checkedNum > 0) {
//         $('.generate').removeAttr("disabled");
//     }
// });


// generatehtml-modal

// $(document).on('click','.showmodal, .speechmodal',function(){
//     // $('#generatehtml').modal('show');
//     // setTimeout(function() {
//     //     $('.generate-box').hide();
//     //     $('.sucess-box').show();
//     // }, 2000);
//     file = $(this).closest('tr').find('.html_file_name').text()
    
// });



// navigation-active-js
$('.menubar ul.menu > li > a').click(function() {
    // $(this).next('.sub_menu').slideToggle(100);
    $(this).parents("li").toggleClass('active_nav');
    $(this).parents("li").siblings().removeClass('active_nav');
});
// end



// datatable
// $('.myTable').DataTable({
//     responsive: true,
//     "bLengthChange": false,
//     "bFilter": false,
// });



// nav-active
jQuery(document).ready(function($) {
    // Get current path and find target link
    var path = window.location.pathname.split("/").pop();
    // Account for home page with empty path
    if (path == '') {
        path = 'index.html';
    }
    var target = $('.sidebar .menubar ul.menu > li > a[href="' + path + '"]');
    //var subtarget = $('.sidebar .navigation .sub_menu ul li a[href="'+path+'"]');
    // Add active class to target link
    target.addClass('active_nav');
    //subtarget.addClass('active_subnav');
    //$('.has_dropdown').find('.active_subnav').parents('.has_dropdown').addClass('active_nav');
});