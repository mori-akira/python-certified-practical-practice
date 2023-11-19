$(() => {
    $('.jp-OutputArea-output').each((_, e) => {
        $(e).click(() => {
            console.log($(e).hasClass());
            if ($(e).hasClass('clicked')) {
                $(e).removeClass('clicked');
            } else {
                $(e).addClass('clicked');
            }
        });
    });
});
