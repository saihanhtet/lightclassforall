$(document).ready(function () {
    $('.display').DataTable({
        "bPaginate": true,
        "bLengthChange": false,
        "bFilter": true,
        "bInfo": false,
        "bAutoWidth": false,
        "pageLength": 3,
    });
});
