#!/bin/sh
src_dir=$(dirname "$0")
config_dir=/home/user/.config
cp -r $config_dir/alacritty $src_dir
cp -r $config_dir/keepmenu $src_dir
cp -r $config_dir/lf $src_dir
cp -r $config_dir/mpv $src_dir
cp -r $config_dir/nvim $src_dir
cp -r $config_dir/qtile $src_dir
cp -r $config_dir/rofi $src_dir
cp -r $config_dir/picom.conf $src_dir
#cp -r $config_dir/ $src_dir
