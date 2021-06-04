function initialise() {
    $('.paginator').click(function (e) {
        e.preventDefault();
        let next = parseInt(e.target.getAttribute('data-page'));
        $.get('?page=' + next, function (data) {
            $('#project_list').html(data)
                        history.pushState('next', '', '?page=' + next)
            })
        })}
$(document).ready(function (){
    initialise();
    })

$(document).ajaxComplete(function (){
    initialise()
    })
