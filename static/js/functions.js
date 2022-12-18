$(document).ready(function () {
    $('.display').DataTable({
        "bPaginate": true,
        "bLengthChange": false,
        "bFilter": true,
        'bSort':false,
        "bInfo": false,
        "bAutoWidth": false,
        "pageLength": 10,
    });
    $('.display-five').DataTable({
        "bPaginate": false,
        'bSort':false,
        "bLengthChange": false,
        "bFilter": false,
        "bInfo": false,
        "bAutoWidth": false,
        "pageLength": 1,
    });
});

