$(document).ready(function () {

    $("button.ui.right.labeled.icon.button.btn_student_submission").click(e => {
        $('.small.modal')
            .modal('show')
            ;

        // console.log(e.target)
        let assignment_id = e.target.previousElementSibling.innerHTML.trim()
        let i = document.querySelector('div.ui.small.modal > div.content > form.ui.form > input.assignment_id')
        // console.log(i)
        i.setAttribute("value", assignment_id)
    });

    $("#notice").click(() => {
        document.querySelector('div#short_modal.ui.modal > div.content > form.ui.form').setAttribute("action", "/postNotice/")

        document.querySelector('div#short_modal.ui.modal > div.content > form.ui.form > div.field >textarea').innerHTML = ""

        $('#short_modal')
            .modal('show')
            ;
    });

    $(".submission").click(() => {
        $('#longer_modal')
            .modal('show')
            ;
    });

    $("#submission_btn").click(() => {
        $('#assignment')
            .modal('show')
            ;
    });

    $('.ui.checkbox')
        .checkbox()
        ;

    document.querySelectorAll('.edit_notice').forEach(
        arg => {
            arg.addEventListener(
                'click', e => {
                    let id = e.target.previousElementSibling.innerHTML.trim();
                    let content = e.target.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.lastElementChild.firstElementChild.firstElementChild.innerHTML.trim();

                    document.querySelector('div#short_modal.ui.modal > div.content > form.ui.form').setAttribute("action", "/updateNotice/" + id)

                    document.querySelector('div#short_modal.ui.modal > div.content > form.ui.form > div.field >textarea').innerHTML = content

                    $('#short_modal')
                        .modal('show')
                        ;
                }
            )
        }
    )

})