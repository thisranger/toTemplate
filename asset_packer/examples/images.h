#ifndef IMAGES_H
#define IMAGES_H

#include <stdint.h>
#include <stdbool.h>

#ifndef PACKED_ATTR
#define PACKED_ATTR __attribute__((packed))
#endif

typedef struct PACKED_ATTR {
    uint16_t width;
    uint16_t height;
    void* data;
    uint32_t offset;
    struct
    {
        bool colored:1;
        bool alpha:1;
        bool flash:1;
    } flags;
} icon_t;

typedef struct PACKED_ATTR {
    uint16_t millisPerFrame;
    struct
    {
        bool autoStart:1;
        bool repeat:1;
    } flags;
    uint16_t amountOfFrames;
    icon_t* frames;
} animatedIcon_t;

extern icon_t IMAGE_file;
extern icon_t IMAGE_dir_image;

extern animatedIcon_t ANIM_test_anim;

#endif // IMAGES_H