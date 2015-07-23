from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getMultiAdapter
from agsci.subsite import utilities 
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import getUtility

class TagsViewlet(ViewletBase):
    
    index = ViewPageTemplateFile('templates/tags_viewlet.pt')

    def update(self):
        context_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_context_state')
    @property
    def portal_state(self):
        return getMultiAdapter((self.context, self.request),
                                name=u'plone_portal_state')

    @property
    def anonymous(self):
        return self.portal_state.anonymous()

    @property
    def tag_root(self):
        return utilities.getTagRoot(self.context)

    @property
    def normalizer(self):
        return getUtility(IIDNormalizer)

    @property
    def tag_data(self):
        tag_root_url = self.tag_root.absolute_url()
        
        tags = getattr(self.context, 'public_tags', [])
        
        if tags:
            tag_urls = ['%s/tags/%s' % (tag_root_url, self.normalizer.normalize(x)) for x in tags]
            return sorted(zip(tags, tag_urls))

        return []