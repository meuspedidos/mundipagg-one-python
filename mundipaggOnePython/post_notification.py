import xmltodict


def parse_post_notification(xml):
    """This function parse the Xml sent by Mundipagg when notify a change in a transaction."""
    return xmltodict.parse(xml)
