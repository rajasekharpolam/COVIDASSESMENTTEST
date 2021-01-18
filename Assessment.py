#!/usr/bin/python
import wx

Static_list = ["Are you suffering with any of  like Diabetes, Hypertension,Heart Disease","Are you experiencing any of the symptoms like cold,fever, difficulty in Breathing, loss of senses of smell and taste","Have you traveled anywhere internationally in the last 30 days","Did you recently interacted with person who has tested Positive for COVID-19","Did you recently visted any COVID containment zones"]

class Button(wx.Frame):
    def __init__(self,parent):
        
        wx.Frame.__init__(self,parent,size = (300,200),id = wx.ID_ANY,pos = wx.DefaultPosition,style = wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU,title="COVID Assesment")
        
        self.count = 0
        self.check_activated_list = []
        
        self.SetBackgroundColour('white')
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        self.Static = wx.StaticText(self,wx.ID_ANY,"Please click on Start button to \ntake Assesment test",style = wx.ALIGN_CENTER)
        self.Vbox.Add(self.Static,1,wx.ALL,3)
        self.but = wx.Button(self,wx.ID_ANY,'Start',wx.DefaultPosition,wx.DefaultSize,0)
        self.Vbox.Add(self.but,0,wx.ALIGN_RIGHT,3)
        self.Bind(wx.EVT_BUTTON,self.click)
        self.SetSizer(self.Vbox)
        self.Show()
        self.Hbox = None
        self.c1 = None
        self.c2 = None
        self.modal = None
        
        
        
    
    def template_creation(self):
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        self.Static = wx.StaticText(self,wx.ID_ANY,Static_list[self.count],wx.DefaultPosition,wx.DefaultSize,0)
        self.Vbox.Add(self.Static,1,wx.ALL,3)
        self.Hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        self.c1 = wx.CheckBox(self,label = 'True')
        self.c2 = wx.CheckBox(self,label = 'False')
        self.Hbox.Add(self.c1,1,wx.ALL,5)
        self.Hbox.Add(self.c2,1,wx.ALL,5)
        self.Vbox.Add(self.Hbox,0,wx.ALL,5)
        if self.count==(len(Static_list)-1):  
            label = "Submit"
        else:
            label = "Next"
        self.but = wx.Button(self,wx.ID_ANY,label,wx.DefaultPosition,wx.DefaultSize,0)
        self.Vbox.Add(self.but,0,wx.ALIGN_RIGHT,3)
        
        
        self.Bind(wx.EVT_BUTTON,self.click)
  
        self.SetSizer(self.Vbox)

        self.Show()
        self.count+=1
        self.change_frame_size(300+self.count,200+self.count)
        
    def change_frame_size(self,width,height):
        self.SetSize(wx.Size(width,height))
    def click(self,e):
        bu = e.GetEventObject()
        if bu.GetLabel() == "Start":
            self.but.Destroy()
            self.Static.Destroy()

            self.but = None
            self.Static= None
            self.count = 0
            if self.count < len(Static_list):
                self.template_creation()
        elif bu.GetLabel() == "Retake Test":
            self.count = 0
            self.but.Destroy()
            self.Static.Destroy()

            self.but = None
            self.Static = None
            self.template_creation()
        else:
            if (not((self.c1.GetValue()) ^ (self.c2.GetValue()))):
                self.modal = wx.MessageDialog(self,message = "Please select only one button",caption = "Informative message")
                self.modal.ShowModal()
            elif bu.GetLabel() == "Submit":
                
                self.c1.Destroy()
                self.c2.Destroy()
                self.but.Destroy()
                self.Static.Destroy()

                self.c1 = None
                self.c2 = None
                self.but = None
                self.Static = None
                self.result()
            elif ((self.c1.GetValue()) ^ (self.c2.GetValue())):
                Button_value = self.c1.GetLabel() if self.c1.GetValue() else self.c2.GetLabel()
            
                self.check_activated_list.append(Button_value)
                self.c1.Destroy()
                self.c2.Destroy()
                self.but.Destroy()
                self.Static.Destroy()

                self.c1 = None
                self.c2 = None
                self.but = None
                self.Static = None
            
                if self.count < len(Static_list):
                    self.template_creation()
        
        
   
        
    def result(self):
        
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.Static = wx.StaticText(self,wx.ID_ANY,style = wx.ALIGN_CENTER)
        label = "Infection rate is\n"
        self.font = wx.Font(18,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
        if 'True' in self.check_activated_list[1:]:
            label+=' HIGH'
            self.Static.SetForegroundColour((255,0,0))
        else:
            label+=" Low"
            self.Static.SetForegroundColour((0,255,0))
        self.Static.SetLabel(label)
        self.Static.SetFont(self.font)
        self.SetBackgroundColour('white')
        
        self.Vbox.Add(self.Static,1,wx.ALL,3)
        
        self.but = wx.Button(self,wx.ID_ANY,'Retake Test',wx.DefaultPosition,wx.DefaultSize,0)
        self.Vbox.Add(self.but,0,wx.ALIGN_RIGHT,3)
        
        self.Bind(wx.EVT_BUTTON,self.click)
        self.SetSizer(self.Vbox)
        self.count+=1
        self.change_frame_size(300+self.count,200+self.count)
        
        
if __name__=="__main__":
    ap = wx.App()
    Button(None)
    ap.MainLoop()