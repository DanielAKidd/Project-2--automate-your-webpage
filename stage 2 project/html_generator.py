def html_gen(subheading, concept_description, extra=False):
    """Creates a structured set of html code.

    extra: optional parameter for including a frequent subset of code"""

    html_part1 = """
    <!-- start concept -->
    <section class="concept_holder">

        <h4>"""+ subheading

    html_part2 = """</h4>

        <article class="content">
            """+ concept_description

    html_extra = """

            <!-- example code block -->
            <div class="code_block">

                <!-- example -->
                <div class="example_container">

<code></code>

                    <footer class="code_footer"></footer>
                </div>
                <!-- end example -->

            </div>
            <!-- end example block -->"""

    html_part3 = """
        </article>

        <div class="concept_divider"></div>
    </section>
    <!-- end concept -->
    """
 
    if extra: # if 'extra' is True
        html = html_part1 + html_part2 + html_extra + html_part3
    else:
        html = html_part1 + html_part2 + html_part3
    return html


def print_all_html(full_list):
    """Function takes a list where each element is itself a list, and invokes
       the function 'html_gen' on each of these in turn. 
       Returns full html for all similarly structured concepts.

    full_list: [ [sub-heading, concept description, True/False], [...] ]
    """ 
    all_html = ""

    # unpack the nested list by assigning it's elements in turn
    for subhead, description, extra_html in full_list:
        all_html += html_gen(subhead, description, extra_html)

    return all_html