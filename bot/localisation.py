#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) PublicLeech Author(s)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hello My master @BestzBrothers , \n\nThis is  Telegram Video Compresser Botð  \n\n<b>Please send me any Telegram Video or file . I Will compress the file to your desired Size .</b> \n\nclick /help for more details... \n\nChannel  :@naijabestz"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "ð¥ Downloading your file my master ð¥ \n"
    
    UPLOAD_START = "ð¤ Uploading your File my master ð¤ \n"
    
    COMPRESS_START = "ð Trying to compress... ð"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95gb due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "ð¥ Downloaded in {}\n\nð Compressed in {}\n\nð¤ Uploaded in {}"

    COMPRESS_PROGRESS = "â³ ETA: {}\nð Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "â Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "â Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "â Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "â ï¸ Already One Process going on. \n or \n A media already exists. \n  Please send /cancel to delete existing media. â ï¸"
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi am Video Compressor Bot \n\n1. Send your telegram video file \n2. Reply the file - /compress And Percentage \nEg:- <code>/compress 50</code> \n\nSupport @BestzBrothers"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
