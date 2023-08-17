#!/bin/sh
draw() {
  ~/.config/lf/draw_img.sh "$@"
  exit 1
}

hash() {
  printf '%s/.cache/lf/%s' "$HOME" \
    "$(stat --printf '%n\0%i\0%F\0%s\0%W\0%Y' -- "$(readlink -f "$1")" | sha256sum | awk '{print $1}')"
}

cache() {
  if [ -f "$1" ]; then
    draw "$@"
  fi
}

file="$1"
shift

if [ -n "$FIFO_UEBERZUG" ]; then
  case "$(file -Lb --mime-type -- "$file")" in
    image/*svg*)
      cache="$(hash "$file").jpg"
      cache "$cache" "$@"
      gm convert "$file" "$cache"
      draw "$cache" "$@"
      ;;
    image/*)
      orientation="$(identify -format '%[EXIF:Orientation]\n' -- "$file")"
      if [ -n "$orientation" ] && [ "$orientation" != 1 ]; then
        cache="$(hash "$file").jpg"
        cache "$cache" "$@"
        convert -- "$file" -auto-orient "$cache"
        draw "$cache" "$@"
      else
        draw "$file" "$@"
      fi
      ;;
    video/*)
      cache="$(hash "$file").jpg"
      cache "$cache" "$@"
      ffmpeg -y -i "$file" -vframes 1 "$cache"
      draw "$cache" "$@"
      ;;
    */pdf)
      cache="$(hash "$file").jpg"
      cache "$cache" "$@"
      gs -o "$cache" -sDEVICE=pngalpha -dLastPage=1 "$file" >/dev/null
      ffmpeg -y -i "$file" -vframes 1 "$cache"
      draw "$cache" "$@"
      ;;
    application/octet-stream) sed "s/\x0/ _ /" "$file" ;;
    application/*) 7z l -ba "$file" | perl -ne 'my @a = split / +/; for my $i (5 .. $#a){ print "$a[$i] "};' ;;
    *) cat "$file" ;;
  esac
fi

file -Lb -- "$1" | fold -s -w "$width"
exit 0
