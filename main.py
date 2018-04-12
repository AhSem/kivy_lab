from kivy.app import App
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.properties import ObjectProperty
from kivy.uix.actionbar import ActionBar, ActionPrevious
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

RootApp = None

SidePanel_AppMenu = {
	'Label':['on_label',None],
	'Button':['on_button',None],
	'CheckBox':['on_checkbox',None],
	'Image':['on_image',None],
	'Slider':['on_slider',None],
	'Progress Bar':['on_progressbar',None],
	'Text Input':['on_textinput',None],
	'Toggle Button':['on_togglebutton',None],
	'Switch':['on_switch',None],
	'Video':['on_video',None],
}

id_AppMenu_METHOD = 0
id_AppMenu_PANEL = 1


##########################################################
#### Page Classes                                     ####
##########################################################
class LabelPage(BoxLayout):
	label = ObjectProperty()

	def __init__(self, **kwargs):
		super(LabelPage, self).__init__( **kwargs)

	def update_text(self, text_input):
		self.label.text = text_input.text

	def update_font_size(self, text_input):
		self.label.font_size = text_input.text


class ButtonPage(BoxLayout):
	pass

class CheckBoxPage(BoxLayout):
	pass

class ImagePage(BoxLayout):
	pass

class SliderPage(BoxLayout):
	pass

class ProgressBarPage(BoxLayout):
	pass

class TextInputPage(BoxLayout):
	pass

class ToggleButtonPage(BoxLayout):
	pass

class SwitchPage(BoxLayout):
	pass

class VideoPage(BoxLayout):
	pass

##########################################################


class ActionMenu(ActionPrevious):
	def menu(self):
		RootApp.toggle_sidepanel()


class AppActionBar(ActionBar):
	pass


class MainPanel(BoxLayout):
	pass


class MenuItem(Button):
	def __init__(self, **kwargs):
		super(MenuItem, self).__init__( **kwargs)
		self.bind(on_press=self.menuitem_selected)

	def menuitem_selected(self, *args):
		print(self.text, SidePanel_AppMenu[self.text], SidePanel_AppMenu[self.text][id_AppMenu_METHOD])
		try:
			function_to_call = SidePanel_AppMenu[self.text][id_AppMenu_METHOD]
		except:
			return
		getattr(RootApp, function_to_call)()


class SidePanel(BoxLayout):
	pass


class NavDrawer(NavigationDrawer):
	def __init__(self, **kwargs):
		super(NavDrawer, self).__init__( **kwargs)

	def close_sidepanel(self, animate=True):
		if self.state == 'open':
			if animate:
				self.anim_to_state('closed')
			else:
				self.state = 'closed'

class KivyLab(App):
	
	def build(self):
		global RootApp
		RootApp = self

		self.navigationdrawer = NavDrawer()

		side_panel = SidePanel()
		self.navigationdrawer.add_widget(side_panel)

		self.main_panel = MainPanel()
		self.navigationdrawer.add_widget(self.main_panel)

		return self.navigationdrawer

	def toggle_sidepanel(self):
	   self.navigationdrawer.toggle_state()

	def on_label(self):
		self._switch_main_page('Label', LabelPage)

	def on_button(self):
		self._switch_main_page('Button', ButtonPage)

	def on_checkbox(self):
		self._switch_main_page('CheckBox', CheckBoxPage)

	def on_image(self):
		self._switch_main_page('Image', ImagePage)

	def on_slider(self):
		self._switch_main_page('Slider', SliderPage)

	def on_progressbar(self):
		self._switch_main_page('Progress Bar', ProgressBarPage)

	def on_textinput(self):
		self._switch_main_page('Text Input',TextInputPage)

	def on_togglebutton(self):
		self._switch_main_page('Toggle Button', ToggleButtonPage)

	def on_switch(self):
		self._switch_main_page('Switch', SwitchPage)

	def on_video(self):
		self._switch_main_page('Video', VideoPage)

	def _switch_main_page(self, key, panel):
		self.navigationdrawer.close_sidepanel()

		if not SidePanel_AppMenu[key][id_AppMenu_PANEL]:
			SidePanel_AppMenu[key][id_AppMenu_PANEL] = panel()

		main_panel = SidePanel_AppMenu[key][id_AppMenu_PANEL]
		self.navigationdrawer.remove_widget(self.main_panel)
		self.navigationdrawer.add_widget(main_panel)
		self.main_panel = main_panel

if __name__ == '__main__':
	KivyLab().run()