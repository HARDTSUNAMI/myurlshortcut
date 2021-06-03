function initialiseForward() {
    $('#load').click(function (e) {
        e.preventDefault();
        let page = parseInt(e.target.getAttribute('data-page'));
        $.get('?page=' + page, function (data) {
            $('#project_list').html(data)
                        history.pushState('page', '', '?page=' + page)

                })
            })
        }
        $(document).ready(function (){
        initialiseForward();
        })
        $(document).ajaxComplete(function (){
        initialiseForward();
        });




function initialiseBack() {
    $('#prev').click(function () {
        window.onpopstate = function () {
            history.go();
            };
        })
    }
        $(document).ready(function (){
        initialiseBack();
    })

        $(document).ajaxComplete(function (){
        initialiseBack()
        location.reload();
    })


