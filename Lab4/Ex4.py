def build_xml_element(tag, content, **attributes):
    attrs = ' '.join(f'{key}="{value}"' for key, value in attributes.items())
    return f'<{tag} {attrs}>{content}</{tag}>'

result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(result)