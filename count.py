# -*- coding: utf-8 -*- 

import wx
import wx.xrc


class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 233,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.Size( 240,100 ), 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial Black" ) )
		self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"瑞幸咖啡 22 元杯数:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,25 ), 0 )
		bSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"瑞幸咖啡 25 元杯数:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,25 ), 0 )
		bSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"瑞幸咖啡 28 元杯数:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,25 ), 0 )
		bSizer1.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"瑞幸咖啡优惠券折扣:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,25 ), 0 )
		bSizer1.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"瑞幸咖啡优惠券使用的咖啡金额:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,25 ), 0 )
		bSizer1.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"EVALUATE", wx.DefaultPosition, wx.Size( 240,65 ), 0 )
		self.m_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		self.m_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		# 
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"CLOSE", wx.DefaultPosition, wx.Size( 240,65 ), 0 )
		self.m_button10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		self.m_button10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		bSizer1.Add( self.m_button10, 0, wx.ALL, 5 )
		# 
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.doEval )
		self.m_button10.Bind( wx.EVT_BUTTON, self.doClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def doEval( self, event ):
		try:
			coffee_22 = int(self.m_textCtrl2.GetValue())
			flag1 = 1
		except:
			coffee_22 = int('0')
			flag1 = 0
		try:
			coffee_25 = int(self.m_textCtrl3.GetValue())
			flag2 = 1
		except:
			coffee_25 = int('0')
			flag2 = 0
		try:
			coffee_28 = int(self.m_textCtrl4.GetValue())
			flag3 = 1
		except:
			coffee_28 = int('0')
			flag3 = 0

		people = coffee_22 + coffee_25 + coffee_28
		try:
			quan = float(self.m_textCtrl5.GetValue()) * 0.1
		except:
			quan = int('1')
		try:
			quan_coffee = int(self.m_textCtrl6.GetValue())
		except:
			quan_coffee = int('0')

		if quan_coffee == 22:
			reduction = 10.4 - 22 * quan
		elif quan_coffee == 25:
			reduction = 11.4 - 25 * quan
		elif quan_coffee == 28:
			reduction = 12.4 - 28 * quan
		else:
			reduction = 0

		average = reduction / people

		if flag1 == 0 and flag2 == 0 and flag3 ==1:
			self.m_staticText1.SetLabel("\n瑞幸 28 元咖啡应支付 " + str(12.4 - average) + " 元")
		if flag1 == 0 and flag2 == 1 and flag3 ==0:
			self.m_staticText1.SetLabel("\n瑞幸 25 元咖啡应支付 " + str(11.4 - average) + " 元")
		if flag1 == 0 and flag2 == 1 and flag3 ==1:
			self.m_staticText1.SetLabel( "\n瑞幸 25 元咖啡应支付 " + str(11.4 - average) + " 元\n瑞幸 28 元咖啡应支付 " + str(12.4 - average) + " 元")
		if flag1 == 1 and flag2 == 0 and flag3 ==0:
			self.m_staticText1.SetLabel("\n瑞幸 22 元咖啡应支付 " + str(10.4 - average) + " 元")
		if flag1 == 1 and flag2 == 0 and flag3 ==1:
			self.m_staticText1.SetLabel("\n瑞幸 22 元咖啡应支付 " + str(10.4 - average) + " 元\n瑞幸 28 元咖啡应支付 " + str(12.4 - average) + " 元")
		if flag1 == 1 and flag2 == 1 and flag3 ==0:
			self.m_staticText1.SetLabel("\n瑞幸 22 元咖啡应支付 " + str(10.4 - average) + " 元\n瑞幸 25 元咖啡应支付 " + str(11.4 - average) + " 元")
		if flag1 == 1 and flag2 == 1 and flag3 ==1:
			self.m_staticText1.SetLabel("\n瑞幸 22 元咖啡应支付 " + str(10.4 - average) + " 元\n瑞幸 25 元咖啡应支付 " + str(11.4 - average) + " 元\n瑞幸 28 元咖啡应支付 " + str(12.4 - average) + " 元")
		
	def doClose(self, event):
		self.Close()

app = wx.App()
frame = MyFrame1(None)
frame.Show()
app.MainLoop()