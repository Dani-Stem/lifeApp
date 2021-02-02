var la_id_v = msg.payload['la_id'];
var la_entry_dateTime_v = msg.payload['la_entry_dateTime'];
var la_mood_v = msg.payload['la_mood'];
var la_recent_activity_v = msg.payload['la_recent_activity'];
var la_goals_complete_v = msg.payload['la_goals_complete'];
var la_mens_v = msg.payload['la_mens'];
var la_next_activity_v = msg.payload['la_next_activity'];

if (la_mood_v != null)
{
    msg.topic = 'insert into la(la_mood)values(la_mood)';
}
else
{
    msg.topic = 'plz answer the question'
}

return msg;


var la_enrty_dateTime_v = + new Date();
var la_mood_v = msg.payload['la_mood'] ;
var la_recent_activity_v = msg.payload['la_recent_activity'] ;
var la_goals_complete_v = msg.payload['la_goals_complete'] ;
var la_mens_v = msg.payload['la_mens'] ;
var la_next_activity_v = msg.payload['la_next_activity'] ;


msg.topic = 'INSERT INTO la(la_entry_dateTime,la_mood,la_recent_activity,la_goals_complete, la_mens,la_next_activity) VALUES(\"' +  la_enrty_dateTime_v + '\",\"' + la_mood_v + '\",\"' + la_recent_activity_v + '\",\"' + la_goals_complete_v + '\",\"' + la_mens_v + '\",\"' + la_next_activity_v +'\")';

return msg;
