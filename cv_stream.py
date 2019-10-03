#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

URL = "http://172.29.156.201:8081/"
s_video = cv2.VideoCapture(URL)

while True:
  ret, img = s_video.read()
  cv2.imshow("Stream Video",img)
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'): break