from typing import override

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile


class GnomeProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('GNOME', ProfileType.DesktopEnv)

	@property
	@override
	def packages(self) -> list[str]:
		return [
			'gnome-backgrounds',
			'gnome-calculator',
			'gnome-calendar',
			'gnome-characters',
			'gnome-clocks',
			'gnome-disk-utility',
			'gnome-font-viewer',
			'gnome-software',
			'flatpak',
			'gnome-system-monitor',
			'gnome-text-editor',
			'gnome-weather',
			'loupe',

			'gdm',
			'gnome-color-manager',
			'gnome-control-center',
			'gnome-keyring',
			'gnome-menus',
			'gnome-session',
			'gnome-settings-daemon',
			'gnome-shell',
			'gnome-user-share',
			'grilo-plugins',
			"gvfs",
			"gvfs-afc",
			"gvfs-dnssd",
			"gvfs-goa",
			"gvfs-google",
			"gvfs-gphoto2",
			"gvfs-mtp",
			"gvfs-nfs",
			"gvfs-onedrive",
			"gvfs-smb",
			"gvfs-wsdd",
			'malcontent',
			'nautilus',
			'rygel',
			'orca',
			'snapshot',
			'sushi',
			'tecla',
			'xdg-desktop-portal-gnome',
			'xdg-user-dirs-gtk',
		]

	@property
	@override
	def default_greeter_type(self) -> GreeterType:
		return GreeterType.Gdm
