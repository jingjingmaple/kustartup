function formatDate(date) {
    var d = new Date(date),
            month = '' + (d.getMonth() + 1),
            day = '' + d.getDate(),
            year = d.getFullYear();

    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;

    return [year, month, day].join('-');
}
function getAvailableRoom() {
    var servicetype = $('#servicetype').val();
    var starttime = $('#starttime').val().replace("T", " ");
    var stoptime = $('#stoptime').val().replace("T", " ");
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
            method: "POST",
            data: { "starttime": starttime, "stoptime": stoptime, "servicetype": servicetype, csrfmiddlewaretoken: csrftoken },
            url: "/api/search",

    })
            .done(function (data2) {
                    data = data2.data;
                    var htmlresult = "<h3>Result</h3>";
                    for (i = 0; i < data.length; i++) {
                            htmlresult = htmlresult + `<div class="card" style="width: 18rem;">
                                    <div class="card-body">
                                    <h5 class="card-title">`+ data[i].name + `</h5>
                                    <h6 class="card-subtitle mb-2 text-muted">`+ data[i].location + `</h6>
                                    
                                    <a href="#" class="card-link" data-toggle="modal" data-target="#loginmodal">Reserve</a>

                                    </div>
                                    </div><br>`;
                    }
                    $('#searchresult').html(htmlresult);


            });
}