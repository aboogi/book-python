// Source: https://docs.python.org/3/_static/copybutton.js

$(document).ready(function() {
    /* Add a [>>>] button on the top-right corner of code samples to hide
     * the >>> and ... prompts and the output and thus make the code
     * copyable. */
    var div = $('.highlight-python .highlight,' +
                '.highlight-python3 .highlight,' +
                '.highlight-pycon3 .highlight,' +
                '.highlight-pycon .highlight,' +
                '.highlight-default .highlight');
    var pre = div.find('pre');

    // get the styles from the current theme
    pre.parent().parent().css('position', 'relative');
    var show_text = '▶';
    var show_title = 'Show the output';
    var hide_text = '✘';
    var hide_title = 'Clear the output';
    var border_width = pre.css('border-top-width');
    var border_style = pre.css('border-top-style');
    var border_color = pre.css('border-top-color');
    var button_styles = {
        'cursor':'pointer', 'position': 'absolute', 'top': '5px', 'left': '-30px',
        'border-color': border_color, 'border-style': border_style,
        'border-width': border_width, 'color': border_color, 'text-size': '50%',
        'font-family': 'monospace', 'padding-left': '0.2em', 'padding-right': '0.2em',
        'border-radius': '0 3px 0 0'
    }

    // create and add the button to all the code blocks that contain >>>
    div.each(function(index) {
        var jthis = $(this);
        if (jthis.find('.gp').length > 0) {
            var button = $(`<span class="copybutton">${hide_text}</span>`);
            button.css(button_styles)
            button.attr('title', hide_title);
            button.data('hidden', 'false');
            jthis.prepend(button);
        }
        // tracebacks (.gt) contain bare text elements that need to be
        // wrapped in a span to work with .nextUntil() (see later)
        jthis.find('pre:has(.gt)').contents().filter(function() {
            return ((this.nodeType == 3) && (this.data.trim().length > 0));
        }).wrap('<span>');
    });

    // define the behavior of the button when it's clicked
    $('.copybutton').click(function(e){
        e.preventDefault();
        var button = $(this);

        if (button.data('hidden') === 'false') {
            // hide the code output
            button.parent().find('.go, .gp, .gt').hide();
            button.next('pre').find('.gt').nextUntil('.gp, .go').css('visibility', 'hidden');
            button.attr('title', show_title);
            button.data('hidden', 'true');
            button.text(show_text);
        } else {
            // show the code output
            button.parent().find('.go, .gt').show();
            button.next('pre').find('.gt').nextUntil('.gp, .go').css('visibility', 'visible');
            button.attr('title', hide_title);
            button.data('hidden', 'false');
            button.text(hide_text);
        }

        button.parent().find('.go').each((i, line) => {
            if (line.innerText === '>>>')
                line.style.visibility = 'hidden';
            else if (line.innerText === '<BLANKLINE>')
                line.innerHTML = '';
        })
    });

    // Following code show/hide code listing outputs onload
    // .click() - hides
    // .click().click(); - show
    // if commented out, there will be some artifacts in code listings
    div.each(function(index) {
        $(this).find('.copybutton').click().click();
    });
});

