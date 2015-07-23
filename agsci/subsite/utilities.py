from Products.CMFPlone.interfaces import IPloneSiteRoot
from agsci.subsite.content.interfaces import ITagRoot
from Acquisition import aq_chain

def getTagRoot(context):
    for i in aq_chain(context):
        if IPloneSiteRoot.providedBy(i):
            return i
        if ITagRoot.providedBy(i):
            return i

    # Probably not needed, but just so we return something.
    return context