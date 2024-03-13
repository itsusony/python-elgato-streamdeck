#         Python Stream Deck Library
#      Released under the MIT license
#
#   dean [at] fourwalledcubicle [dot] com
#         www.fourwalledcubicle.com
#

from .StreamDeck import StreamDeck, ControlType, DialEventType, TouchscreenEventType


def _dials_rotation_transform(value):
    if value < 0x80:
        # Clockwise rotation
        return value
    else:
        # Counterclockwise rotation
        return -(0x100 - value)


class StreamDeckPlus(StreamDeck):
    KEY_COUNT = 8
    KEY_COLS = 4
    KEY_ROWS = 2

    DIAL_COUNT = 4

    KEY_PIXEL_WIDTH = 120
    KEY_PIXEL_HEIGHT = 120
    KEY_IMAGE_FORMAT = "JPEG"
    KEY_FLIP = (False, False)
    KEY_ROTATION = 0

    DECK_TYPE = "Stream Deck +"
    DECK_VISUAL = True
    DECK_TOUCH = True

    TOUCHSCREEN_PIXEL_HEIGHT = 100
    TOUCHSCREEN_PIXEL_WIDTH = 800
    TOUCHSCREEN_IMAGE_FORMAT = "JPEG"
    TOUCHSCREEN_FLIP = (False, False)
    TOUCHSCREEN_ROTATION = 0

    _IMG_PACKET_LEN = 1024  # Max size for a data packet when setting images

    _KEY_PACKET_HEADER = 8
    _LCD_PACKET_HEADER = 16

    _KEY_PACKET_PAYLOAD_LEN = _IMG_PACKET_LEN - _KEY_PACKET_HEADER
    _LCD_PACKET_PAYLOAD_LEN = _IMG_PACKET_LEN - _LCD_PACKET_HEADER

    _DIAL_EVENT_TRANSFORM = {
        DialEventType.TURN: _dials_rotation_transform,
        DialEventType.PUSH: bool,
    }

    # 120 x 120 black JPEG
    BLANK_KEY_IMAGE = [
        0xff, 0xd8, 0xff, 0xe0, 0x00, 0x10, 0x4a, 0x46, 0x49, 0x46, 0x00,
        0x01, 0x01, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0xff, 0xdb,
        0x00, 0x43, 0x00, 0x08, 0x06, 0x06, 0x07, 0x06, 0x05, 0x08, 0x07,
        0x07, 0x07, 0x09, 0x09, 0x08, 0x0a, 0x0c, 0x14, 0x0d, 0x0c, 0x0b,
        0x0b, 0x0c, 0x19, 0x12, 0x13, 0x0f, 0x14, 0x1d, 0x1a, 0x1f, 0x1e,
        0x1d, 0x1a, 0x1c, 0x1c, 0x20, 0x24, 0x2e, 0x27, 0x20, 0x22, 0x2c,
        0x23, 0x1c, 0x1c, 0x28, 0x37, 0x29, 0x2c, 0x30, 0x31, 0x34, 0x34,
        0x34, 0x1f, 0x27, 0x39, 0x3d, 0x38, 0x32, 0x3c, 0x2e, 0x33, 0x34,
        0x32, 0xff, 0xdb, 0x00, 0x43, 0x01, 0x09, 0x09, 0x09, 0x0c, 0x0b,
        0x0c, 0x18, 0x0d, 0x0d, 0x18, 0x32, 0x21, 0x1c, 0x21, 0x32, 0x32,
        0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32,
        0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32,
        0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32,
        0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32,
        0x32, 0x32, 0x32, 0x32, 0xff, 0xc0, 0x00, 0x11, 0x08, 0x00, 0x78,
        0x00, 0x78, 0x03, 0x01, 0x22, 0x00, 0x02, 0x11, 0x01, 0x03, 0x11,
        0x01, 0xff, 0xc4, 0x00, 0x1f, 0x00, 0x00, 0x01, 0x05, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a,
        0x0b, 0xff, 0xc4, 0x00, 0xb5, 0x10, 0x00, 0x02, 0x01, 0x03, 0x03,
        0x02, 0x04, 0x03, 0x05, 0x05, 0x04, 0x04, 0x00, 0x00, 0x01, 0x7d,
        0x01, 0x02, 0x03, 0x00, 0x04, 0x11, 0x05, 0x12, 0x21, 0x31, 0x41,
        0x06, 0x13, 0x51, 0x61, 0x07, 0x22, 0x71, 0x14, 0x32, 0x81, 0x91,
        0xa1, 0x08, 0x23, 0x42, 0xb1, 0xc1, 0x15, 0x52, 0xd1, 0xf0, 0x24,
        0x33, 0x62, 0x72, 0x82, 0x09, 0x0a, 0x16, 0x17, 0x18, 0x19, 0x1a,
        0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x34, 0x35, 0x36, 0x37, 0x38,
        0x39, 0x3a, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4a, 0x53,
        0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5a, 0x63, 0x64, 0x65, 0x66,
        0x67, 0x68, 0x69, 0x6a, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78, 0x79,
        0x7a, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8a, 0x92, 0x93,
        0x94, 0x95, 0x96, 0x97, 0x98, 0x99, 0x9a, 0xa2, 0xa3, 0xa4, 0xa5,
        0xa6, 0xa7, 0xa8, 0xa9, 0xaa, 0xb2, 0xb3, 0xb4, 0xb5, 0xb6, 0xb7,
        0xb8, 0xb9, 0xba, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9,
        0xca, 0xd2, 0xd3, 0xd4, 0xd5, 0xd6, 0xd7, 0xd8, 0xd9, 0xda, 0xe1,
        0xe2, 0xe3, 0xe4, 0xe5, 0xe6, 0xe7, 0xe8, 0xe9, 0xea, 0xf1, 0xf2,
        0xf3, 0xf4, 0xf5, 0xf6, 0xf7, 0xf8, 0xf9, 0xfa, 0xff, 0xc4, 0x00,
        0x1f, 0x01, 0x00, 0x03, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x03,
        0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0xff, 0xc4, 0x00,
        0xb5, 0x11, 0x00, 0x02, 0x01, 0x02, 0x04, 0x04, 0x03, 0x04, 0x07,
        0x05, 0x04, 0x04, 0x00, 0x01, 0x02, 0x77, 0x00, 0x01, 0x02, 0x03,
        0x11, 0x04, 0x05, 0x21, 0x31, 0x06, 0x12, 0x41, 0x51, 0x07, 0x61,
        0x71, 0x13, 0x22, 0x32, 0x81, 0x08, 0x14, 0x42, 0x91, 0xa1, 0xb1,
        0xc1, 0x09, 0x23, 0x33, 0x52, 0xf0, 0x15, 0x62, 0x72, 0xd1, 0x0a,
        0x16, 0x24, 0x34, 0xe1, 0x25, 0xf1, 0x17, 0x18, 0x19, 0x1a, 0x26,
        0x27, 0x28, 0x29, 0x2a, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3a, 0x43,
        0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4a, 0x53, 0x54, 0x55, 0x56,
        0x57, 0x58, 0x59, 0x5a, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69,
        0x6a, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7a, 0x82, 0x83,
        0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8a, 0x92, 0x93, 0x94, 0x95,
        0x96, 0x97, 0x98, 0x99, 0x9a, 0xa2, 0xa3, 0xa4, 0xa5, 0xa6, 0xa7,
        0xa8, 0xa9, 0xaa, 0xb2, 0xb3, 0xb4, 0xb5, 0xb6, 0xb7, 0xb8, 0xb9,
        0xba, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xca, 0xd2,
        0xd3, 0xd4, 0xd5, 0xd6, 0xd7, 0xd8, 0xd9, 0xda, 0xe2, 0xe3, 0xe4,
        0xe5, 0xe6, 0xe7, 0xe8, 0xe9, 0xea, 0xf2, 0xf3, 0xf4, 0xf5, 0xf6,
        0xf7, 0xf8, 0xf9, 0xfa, 0xff, 0xda, 0x00, 0x0c, 0x03, 0x01, 0x00,
        0x02, 0x11, 0x03, 0x11, 0x00, 0x3f, 0x00, 0xf9, 0xfe, 0x8a, 0x28,
        0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a,
        0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02,
        0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0,
        0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28,
        0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a,
        0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02,
        0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0,
        0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28,
        0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a,
        0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02,
        0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0,
        0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28,
        0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a,
        0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02,
        0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0,
        0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28,
        0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a,
        0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02,
        0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0,
        0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28,
        0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a,
        0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02,
        0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0, 0x02, 0x8a, 0x28, 0xa0,
        0x0f, 0xff, 0xd9
    ]

    # 120 x 800 black JPEG
    BLANK_TOUCHSCREEN_IMAGE = [
        0xff, 0xd8, 0xff, 0xe0, 0x00, 0x10, 0x4a, 0x46, 0x49, 0x46, 0x00,
        0x01, 0x01, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0xff, 0xdb,
        0x00, 0x43, 0x00, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0xff, 0xdb, 0x00, 0x43, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0xff, 0xc0, 0x00, 0x11, 0x08, 0x03, 0x20,
        0x00, 0x64, 0x03, 0x01, 0x22, 0x00, 0x02, 0x11, 0x01, 0x03, 0x11,
        0x01, 0xff, 0xc4, 0x00, 0x1f, 0x00, 0x00, 0x01, 0x05, 0x01, 0x01,
        0x01, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a,
        0x0b, 0xff, 0xc4, 0x00, 0xb5, 0x10, 0x00, 0x02, 0x01, 0x03, 0x03,
        0x02, 0x04, 0x03, 0x05, 0x05, 0x04, 0x04, 0x00, 0x00, 0x01, 0x7d,
        0x01, 0x02, 0x03, 0x00, 0x04, 0x11, 0x05, 0x12, 0x21, 0x31, 0x41,
        0x06, 0x13, 0x51, 0x61, 0x07, 0x22, 0x71, 0x14, 0x32, 0x81, 0x91,
        0xa1, 0x08, 0x23, 0x42, 0xb1, 0xc1, 0x15, 0x52, 0xd1, 0xf0, 0x24,
        0x33, 0x62, 0x72, 0x82, 0x09, 0x0a, 0x16, 0x17, 0x18, 0x19, 0x1a,
        0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x34, 0x35, 0x36, 0x37, 0x38,
        0x39, 0x3a, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4a, 0x53,
        0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5a, 0x63, 0x64, 0x65, 0x66,
        0x67, 0x68, 0x69, 0x6a, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78, 0x79,
        0x7a, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8a, 0x92, 0x93,
        0x94, 0x95, 0x96, 0x97, 0x98, 0x99, 0x9a, 0xa2, 0xa3, 0xa4, 0xa5,
        0xa6, 0xa7, 0xa8, 0xa9, 0xaa, 0xb2, 0xb3, 0xb4, 0xb5, 0xb6, 0xb7,
        0xb8, 0xb9, 0xba, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9,
        0xca, 0xd2, 0xd3, 0xd4, 0xd5, 0xd6, 0xd7, 0xd8, 0xd9, 0xda, 0xe1,
        0xe2, 0xe3, 0xe4, 0xe5, 0xe6, 0xe7, 0xe8, 0xe9, 0xea, 0xf1, 0xf2,
        0xf3, 0xf4, 0xf5, 0xf6, 0xf7, 0xf8, 0xf9, 0xfa, 0xff, 0xc4, 0x00,
        0x1f, 0x01, 0x00, 0x03, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
        0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x03,
        0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0xff, 0xc4, 0x00,
        0xb5, 0x11, 0x00, 0x02, 0x01, 0x02, 0x04, 0x04, 0x03, 0x04, 0x07,
        0x05, 0x04, 0x04, 0x00, 0x01, 0x02, 0x77, 0x00, 0x01, 0x02, 0x03,
        0x11, 0x04, 0x05, 0x21, 0x31, 0x06, 0x12, 0x41, 0x51, 0x07, 0x61,
        0x71, 0x13, 0x22, 0x32, 0x81, 0x08, 0x14, 0x42, 0x91, 0xa1, 0xb1,
        0xc1, 0x09, 0x23, 0x33, 0x52, 0xf0, 0x15, 0x62, 0x72, 0xd1, 0x0a,
        0x16, 0x24, 0x34, 0xe1, 0x25, 0xf1, 0x17, 0x18, 0x19, 0x1a, 0x26,
        0x27, 0x28, 0x29, 0x2a, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3a, 0x43,
        0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4a, 0x53, 0x54, 0x55, 0x56,
        0x57, 0x58, 0x59, 0x5a, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69,
        0x6a, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7a, 0x82, 0x83,
        0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8a, 0x92, 0x93, 0x94, 0x95,
        0x96, 0x97, 0x98, 0x99, 0x9a, 0xa2, 0xa3, 0xa4, 0xa5, 0xa6, 0xa7,
        0xa8, 0xa9, 0xaa, 0xb2, 0xb3, 0xb4, 0xb5, 0xb6, 0xb7, 0xb8, 0xb9,
        0xba, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xca, 0xd2,
        0xd3, 0xd4, 0xd5, 0xd6, 0xd7, 0xd8, 0xd9, 0xda, 0xe2, 0xe3, 0xe4,
        0xe5, 0xe6, 0xe7, 0xe8, 0xe9, 0xea, 0xf2, 0xf3, 0xf4, 0xf5, 0xf6,
        0xf7, 0xf8, 0xf9, 0xfa, 0xff, 0xda, 0x00, 0x0c, 0x03, 0x01, 0x00,
        0x02, 0x11, 0x03, 0x11, 0x00, 0x3f, 0x00, 0xff, 0x00, 0x3f, 0xfa,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a,
        0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80,
        0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2,
        0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28, 0xa2, 0x80, 0x0a, 0x28,
        0xa2, 0x80, 0x3f, 0xff, 0xd9
    ]

    def _reset_key_stream(self):
        payload = bytearray(self._IMG_PACKET_LEN)
        payload[0] = 0x02
        self.device.write(payload)

    def reset(self):
        payload = bytearray(32)
        payload[0:2] = [0x03, 0x02]
        self.device.write_feature(payload)

    def _read_control_states(self):
        states = self.device.read(14)

        if states is None:
            return None

        states = states[1:]

        if states[0] == 0x00: # Key Event
            new_key_states = [bool(s) for s in states[3:]]

            return {
                ControlType.KEY: new_key_states
            }
        elif states[0] == 0x02: # Touchscreen Event
            if states[3] == 1:
                event_type = TouchscreenEventType.SHORT
            elif states[3] == 2:
                event_type = TouchscreenEventType.LONG
            elif states[3] == 3:
                event_type = TouchscreenEventType.DRAG
            else:
                return None

            value = {
                'x': (states[6] << 8) + states[5],
                'y': (states[8] << 8) + states[7]
            }

            if event_type == TouchscreenEventType.DRAG:
                value["x_out"] = (states[10] << 8) + states[9]
                value["y_out"] = (states[12] << 8) + states[11]

            return {
                ControlType.TOUCHSCREEN: (event_type, value),
            }
        elif states[0] == 0x03: # Dial Event
            if states[3] == 0x01:
                event_type = DialEventType.TURN
            elif states[3] == 0x02:
                event_type = DialEventType.PUSH
            else
                return None

            values = [self._DIAL_EVENT_TRANSFORM[event_type](s) for s in states[4:4 + self.DIAL_COUNT]]

            return {
                ControlType.DIAL: {
                    event_type: values,
                }
            }

    def set_brightness(self, percent):
        if isinstance(percent, float):
            percent = int(100.0 * percent)

        percent = min(max(percent, 0), 100)

        payload = bytearray(32)
        payload[0:3] = [0x03, 0x08, percent]

        self.device.write_feature(payload)

    def get_serial_number(self):
        serial = self.device.read_feature(0x06, 32)
        return self._extract_string(serial[5:])

    def get_firmware_version(self):
        version = self.device.read_feature(0x05, 32)
        return self._extract_string(version[5:])

    def set_key_image(self, key, image):
        if min(max(key, 0), self.KEY_COUNT) != key:
            raise IndexError("Invalid key index {}.".format(key))

        image = bytes(image or self.BLANK_KEY_IMAGE)

        page_number = 0
        bytes_remaining = len(image)
        while bytes_remaining > 0:
            this_length = min(bytes_remaining, self._KEY_PACKET_PAYLOAD_LEN)

            header = [
                0x02,                                           # 0
                0x07,                                           # 1
                key & 0xff,                                     # 2 key_index
                1 if this_length == bytes_remaining else 0,     # 3 is_last
                this_length & 0xff,                             # 4 bytecount low byte
                (this_length >> 8) & 0xff,                      # 5 bytecount high byte
                page_number & 0xff,                             # 6 pagenumber low byte
                (page_number >> 8) & 0xff,                      # 7 pagenumber high byte
            ]

            bytes_sent = page_number * (self._KEY_PACKET_PAYLOAD_LEN)
            payload = bytes(header) + image[bytes_sent:bytes_sent + this_length]
            padding = bytearray(self._IMG_PACKET_LEN - len(payload))
            self.device.write(payload + padding)
            bytes_remaining = bytes_remaining - this_length
            page_number = page_number + 1

    def set_touchscreen_image(self, image, x_pos=0, y_pos=0, width=0, height=0):
        if not image:
            image = self.BLANK_TOUCHSCREEN_IMAGE
            x_pos = 0
            y_pos = 0
            width = self.TOUCHSCREEN_PIXEL_WIDTH
            height = self.TOUCHSCREEN_PIXEL_HEIGHT

        if min(max(x_pos, 0), self.TOUCHSCREEN_PIXEL_WIDTH) != x_pos:
            raise IndexError("Invalid x position {}.".format(x_pos))

        if min(max(y_pos, 0), self.TOUCHSCREEN_PIXEL_HEIGHT) != y_pos:
            raise IndexError("Invalid y position {}.".format(y_pos))

        if min(max(width, 1), self.TOUCHSCREEN_PIXEL_WIDTH - x_pos) != width:
            raise IndexError("Invalid draw width {}.".format(width))

        if min(max(height, 1), self.TOUCHSCREEN_PIXEL_HEIGHT - y_pos) != height:
            raise IndexError("Invalid draw height {}.".format(height))

        image = bytes(image)

        page_number = 0
        bytes_remaining = len(image)
        while bytes_remaining > 0:
            this_length = min(bytes_remaining, self._LCD_PACKET_PAYLOAD_LEN)
            bytes_sent = page_number * self._LCD_PACKET_PAYLOAD_LEN

            header = [
                0x02,  # 0
                0x0c,  # 1
                x_pos & 0xff,  # 2 xpos low byte
                (x_pos >> 8) & 0xff,  # 3 xpos high byte
                y_pos & 0xff,  # 4 ypos low byte
                (y_pos >> 8) & 0xff,  # 5 ypos high byte
                width & 0xff,  # 6 width low byte // 120
                (width >> 8) & 0xff,  # 7 width high byte
                height & 0xff,  # 8 height low byte // 120
                (height >> 8) & 0xff,  # 9 height high byte
                1 if this_length == bytes_remaining else 0,  # 10 is the last report?
                page_number & 0xff,  # 12 pagenumber low byte
                (page_number >> 8) & 0xff,  # 11 pagenumber high byte
                this_length & 0xff,  # 14 bytecount high byte
                (this_length >> 8) & 0xff,  # 13 bytecount high byte
                0x00,  # 15 padding
            ]

            payload = bytes(header) + image[bytes_sent:bytes_sent + this_length]
            padding = bytearray(self._IMG_PACKET_LEN - len(payload))
            self.device.write(payload + padding)

            bytes_remaining = bytes_remaining - this_length
            page_number = page_number + 1
