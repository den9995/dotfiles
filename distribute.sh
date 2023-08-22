#!/bin/sh
src_dir=$(dirname "$0")
config_dir=/home/user/.config
set -x
cp -r $src_dir/alacritty  $config_dir
cp -r $src_dir/keepmenu   $config_dir
cp -r $src_dir/lf         $config_dir
cp -r $src_dir/mpv        $config_dir
cp -r $src_dir/nvim       $config_dir
cp -r $src_dir/qtile      $config_dir
cp -r $src_dir/rofi       $config_dir
cp -r $src_dir/picom.conf $config_dir
#cp -r $src_dir/           $config_dir
