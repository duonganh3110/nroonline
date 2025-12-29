[app]
title = NRO Online
package.name = nroonline
package.domain = org.duonganh
source.dir = .
source.include_exts = py,png,jpg,jpeg,webp,ttf,otf,json,txt,mp3,wav,ogg

# Nếu game em là pygame thì để pygame (có thể vẫn khó build)
requirements = python3,pygame

android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET
