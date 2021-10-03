(function ($) {

})(django.jQuery);

$(function () {
    var url = "/subCategoriesData/";

    // Edit
    if ($("#id_category").val() == "") {
        $("#id_sub_category").html('<option value="">---------</option>');
    }
    else
    {
        var categoryid = $("#id_category").val()
        var id_sub_category = $("#id_sub_category").val()
        $.ajax({
            url: url,
            data: {
                'categoryid': categoryid
            },
            success: function (data) {
                var options = '<option value="">---------</option>';
                for (var i = 0; i < data['sub_categories_data'].length; i++) {
                    if (id_sub_category == data['sub_categories_data'][i]['id']){
                        options += '<option value="' + data['sub_categories_data'][i]['id'] + '" selected>' + data['sub_categories_data'][i]['name'] + "</option>";
                    }else{
                        options += '<option value="' + data['sub_categories_data'][i]['id'] + '">' + data['sub_categories_data'][i]['name'] + "</option>";
                    }
                }
                $("#id_sub_category").html(options);
            }
        });
    }
    // Add
    $("#id_category").change(function () {
        var categoryid = $(this).val()
        
        $.ajax({ 
            url: url, 
            data: {
                'categoryid': categoryid
            },
            success: function (data) { 
                var options = '<option value="">---------</option>';
                for (var i = 0; i < data['sub_categories_data'].length ; i++) {
                    options += '<option value="' + data['sub_categories_data'][i]['id'] + '">' + data['sub_categories_data'][i]['name'] + "</option>";
                }
                $("#id_sub_category").html(options);
            }
        });
    });
});
