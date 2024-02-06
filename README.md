# Description

A tiny application intended to provide "virtual presence" with your team, without giving your company's security team headaches.  
The initial version intends to use a shared folder (i.e. OneDrive, DropBox, etc) as a data source.

A typical workflow would involve:  
- Enter a room
- Assign that room a meeting link (i.e. Slack Huddle, Teams Meeting, WebEx, etc)
- Another user enters the room and is prompted to join your meeting link.

This workflow allows you to keep your actual meetings behind tools your security teams already control, while getting the benefit of "virtual presence" or in other terms, it allows you to keep track of how your team is working throughout a day.  All the benefits of being in an office, with none of the downsides.

# Dependencies
- nativegui
- pywebview
- pydispatcher
