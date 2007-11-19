# -*- coding: UTF-8 -*-
# Copyright (C) 2006-2007 Hervé Cauwelier <herve@itaapy.com>
# Copyright (C) 2006-2007 Juan David Ibáñez Palomar <jdavid@itaapy.com>
# Copyright (C) 2007 Sylvain Taverne <sylvain@itaapy.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Import from itools
from itools.pdf import PDFFile
from itools.stl import stl
from itools.handlers import Image as ImageFile

# Import from ikaaro
from file import File
from registry import register_object_class


###########################################################################
# Images, Video & Flash
###########################################################################
class Image(File):

    class_id = 'image'
    class_title = u'Image'
    class_icon16 = 'images/Image16.png'
    class_icon48 = 'images/Image48.png'
    class_views = [['view'],
                   ['externaledit', 'upload_form'],
                   ['edit_metadata_form'],
                   ['state_form'],
                   ['history_form']]
    class_handler = ImageFile


    # XXX Temporal, until icon's API is fixed
    def icons_path(self):
        return ';icon48?width=144&height=144'


    icon48__access__ = True
    def icon48(self, context):
        width = context.get_form_value('width', 48)
        height = context.get_form_value('height', 48)
        width, height = int(width), int(height)

        handler = self.handler
        data, format = handler.get_thumbnail(width, height)
        if data is None:
            data = self.get_object('/ui/images/Image48.png').to_str()
            format = 'png'

        response = context.response
        response.set_header('Content-Type', 'image/%s' % format)
        return data


    view__access__ = 'is_allowed_to_view'
    view__label__ = u'View'
    view__sublabel__ = u'View'
    def view(self, context):
        handler = self.get_object('/ui/binary/Image_view.xml')
        return handler.to_str()



class Video(File):

    class_id = 'video'
    class_title = u'Video'
    class_description = u'Video'
    class_icon16 = 'images/Flash16.png'
    class_icon48 = 'images/Flash48.png'


    view__access__ = 'is_allowed_to_view'
    view__label__ = u'View'
    view__sublabel__ = u'View'
    def view(self, context):
        namespace = {}
        namespace['format'] = self.get_mimetype()

        handler = self.get_object('/ui/binary/Video_view.xml')
        return stl(handler, namespace)


    def get_content_type(self):
        # XXX For some reason when uploading a WMV file with firefox the
        # file is identified as "video/x-msvideo". But IE does not understand
        # it, instead it expects "video/x-ms-wmv".
        return self.get_mimetype()



class Flash(File):

    class_id = 'application/x-shockwave-flash'
    class_title = u'Flash'
    class_description = u'Flash Document'
    class_icon16 = 'images/Flash16.png'
    class_icon48 = 'images/Flash48.png'


    view__label__ = u'View'
    view__sublabel__ = u'View'
    view__access__ = 'is_allowed_to_view'
    def view(self, context):
        handler = self.get_object('/ui/binary/Flash_view.xml')
        return stl(handler)


###########################################################################
# Office Documents
###########################################################################
class MSWord(File):

    class_id = 'application/msword'
    class_title = u'Word'
    class_description = u'Word Text'
    class_icon16 = 'images/Word16.png'
    class_icon48 = 'images/Word48.png'



class MSExcel(File):

    class_id = 'application/vnd.ms-excel'
    class_title = u'Excel'
    class_description = u'Excel Spreadsheet'
    class_icon16 = 'images/Excel16.png'
    class_icon48 = 'images/Excel48.png'



class MSPowerPoint(File):

    class_id = 'application/vnd.ms-powerpoint'
    class_title = u'PowerPoint'
    class_description = u'PowerPoint Presentation'
    class_icon16 = 'images/PowerPoint16.png'
    class_icon48 = 'images/PowerPoint48.png'



class OOWriter(File):

    class_id = 'application/vnd.sun.xml.writer'
    class_title = u'OOo Writer'
    class_description = u'OpenOffice.org Text'
    class_icon16 = 'images/OOWriter16.png'
    class_icon48 = 'images/OOWriter48.png'



class OOCalc(File):

    class_id = 'application/vnd.sun.xml.calc'
    class_title = u'OOo Calc'
    class_description = u'OpenOffice.org Spreadsheet'
    class_icon16 = 'images/OOCalc16.png'
    class_icon48 = 'images/OOCalc48.png'



class OOImpress(File):

    class_id = 'application/vnd.sun.xml.impress'
    class_title = u'OOo Impress'
    class_description = u'OpenOffice.org Presentation'
    class_icon16 = 'images/OOImpress16.png'
    class_icon48 = 'images/OOImpress48.png'



class PDF(File):

    class_id = 'application/pdf'
    class_title = u'PDF'
    class_description = u'PDF Document'
    class_icon16 = 'images/Pdf16.png'
    class_icon48 = 'images/Pdf48.png'
    class_handler = PDFFile



class RTF(File):

    class_id = 'text/rtf'
    class_title = u"RTF"
    class_description = u'RTF Document'
    class_icon16 = 'images/Text16.png'
    class_icon48 = 'images/Text48.png'



class ODT(File):

    class_id ='application/vnd.oasis.opendocument.text'
    class_title = u'ODT'
    class_description = u'OpenDocument Text'
    class_icon16 = 'images/Odt16.png'
    class_icon48 = 'images/Odt48.png'



class ODS(File):

    class_id ='application/vnd.oasis.opendocument.spreadsheet'
    class_title = u'ODS'
    class_description = u'OpenDocument Spreadsheet'
    class_icon16 = 'images/Ods16.png'
    class_icon48 = 'images/Ods48.png'



class ODP(File):

    class_id ='application/vnd.oasis.opendocument.presentation'
    class_title = u'ODP'
    class_description = u'OpenDocument Presentation'
    class_icon16 = 'images/Odp16.png'
    class_icon48 = 'images/Odp48.png'



###########################################################################
# Archives
###########################################################################
class Archive(File):

    view__access__ = 'is_allowed_to_view'
    view__label__ = u'View'
    view__sublabel__ = u'View'
    def view(self, context):
        namespace = {}
        contents = self.get_contents()
        namespace['contents'] = '\n'.join(contents)

        handler = self.get_object('/ui/binary/Archive_view.xml')
        return stl(handler, namespace)



class ZipArchive(Archive):

    class_id = 'application/zip'
    class_title = u"Zip"
    class_description = u"Zip Archive"
    class_icon16 = 'images/Zip16.png'
    class_icon48 = 'images/Zip48.png'



class TarArchive(Archive):

    class_id = 'application/x-tar'
    class_title = u"Tar"
    class_description = u"Tar Archive"
    class_icon16 = 'images/Tar16.png'
    class_icon48 = 'images/Tar48.png'


###########################################################################
# Compression
###########################################################################

class Compression(File):
    # TODO API?
    pass



class Gzip(Compression):

    class_id = 'application/x-gzip'
    class_title = u"Gzip"
    class_description = u"Gzip Compressed"
    class_icon16 = 'images/Gzip16.png'
    class_icon48 = 'images/Gzip48.png'




class Bzip2(Compression):

    class_id = 'application/x-bzip2'
    class_title = u"Bzip2"
    class_description = u"Bzip2 Compressed"
    class_icon16 = 'images/Bzip16.png'
    class_icon48 = 'images/Bzip48.png'


###########################################################################
# Register
###########################################################################
register_object_class(Image)
register_object_class(Video)
register_object_class(Flash)
register_object_class(MSWord)
register_object_class(MSExcel)
register_object_class(MSPowerPoint)
register_object_class(PDF)
register_object_class(RTF)
# OpenOffice.org1.0 Format
register_object_class(OOWriter)
register_object_class(OOCalc)
register_object_class(OOImpress)
# OpenOffice.org2.0 Format (ODF)
register_object_class(ODT)
register_object_class(ODS)
register_object_class(ODP)
# Archives
register_object_class(ZipArchive)
register_object_class(TarArchive)
# Compression
register_object_class(Gzip)
register_object_class(Bzip2)
