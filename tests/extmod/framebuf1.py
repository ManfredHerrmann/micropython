try:
    import framebuf
except ImportError:
    print("SKIP")
    import sys
    sys.exit()

w = 5
h = 16
buf = bytearray(w * h // 8)
fbuf = framebuf.FrameBuffer(buf, w, h, framebuf.MVLSB)

# access as buffer
print(memoryview(fbuf)[0])

# fill
fbuf.fill(1)
print(buf)
fbuf.fill(0)
print(buf)

# put pixel
fbuf.pixel(0, 0, 1)
fbuf.pixel(4, 0, 1)
fbuf.pixel(0, 15, 1)
fbuf.pixel(4, 15, 1)
print(buf)

# clear pixel
fbuf.pixel(4, 15, 0)
print(buf)

# get pixel
print(fbuf.pixel(0, 0), fbuf.pixel(1, 1))

# hline
fbuf.fill(0)
fbuf.hline(0, 1, w, 1)
print('hline', buf)

# vline
fbuf.fill(0)
fbuf.vline(1, 0, h, 1)
print('vline', buf)

# rect
fbuf.fill(0)
fbuf.rect(1, 1, 3, 3, 1)
print('rect', buf)

# line
fbuf.fill(0)
fbuf.line(1, 1, 3, 3, 1)
print('line', buf)

# scroll
fbuf.fill(0)
fbuf.pixel(2, 7, 1)
fbuf.scroll(0, 1)
print(buf)
fbuf.scroll(0, -2)
print(buf)
fbuf.scroll(1, 0)
print(buf)
fbuf.scroll(-1, 0)
print(buf)
fbuf.scroll(2, 2)
print(buf)

# print text
fbuf.fill(0)
fbuf.text("hello", 0, 0, 1)
print(buf)
fbuf.text("hello", 0, 0, 0) # clear
print(buf)

# char out of font range set to chr(127)
fbuf.text(str(chr(31)), 0, 0)
print(buf)

# test legacy constructor
fbuf = framebuf.FrameBuffer1(buf, w, h)
fbuf = framebuf.FrameBuffer1(buf, w, h, w)
