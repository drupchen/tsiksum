from textwrap import dedent

head = dedent("""\
    <!-- Last updated for Version 2.1 -->
    
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>ཚིག་གསུམ་གནད་བརྡེག།</title>
        <link rel="stylesheet" href="css/hyperaudio-lite-player.css">
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jomolhari">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.5.0/velocity.js"></script>
        <style>
          /* uncomment the following CSS for active parent / word indicator */ 
          
          
          .hyperaudio-transcript .active{
            background-color: #efefef;
          }
      
          .hyperaudio-transcript .active > .active {
            background-color: #ccf;
            text-decoration:  #00f underline;
            text-decoration-thickness: 3px;
          }
          
          #popover {
          position: absolute;
          background-color: #f9f9f9;
          
          border: 1px solid #ccc;
          padding: 10px;
          border-radius: 4px;
          box-shadow: 0 2px 5px rgba(0,0,0,0.2);
          display: none;
          z-index: 1;
          font-size: small;
          font-family: Jomolhari, Arial,Helvetica Neue,Helvetica,sans-serif;
        }
    
        #popover a {
          text-decoration: none; 
          color: #303030;
          cursor: pointer;
        }
    
        #clipboard-text {
          font-family: Jomolhari, Courier New,Courier,Lucida Sans Typewriter,Lucida Typewriter,monospace; 
        }
    
        #clipboard-confirm {
          font-size: medium;
        }
        </style>
      </head>""")

body_beginning = dedent("""\
      <body>
          <p style="font-size: 32pt; text-align: center; color: brown;">༄༅། །ཚིག་གསུམ་གནད་བརྡེག་གི་ལྗགས་ཁྲིད་གཞུང་ཚིག་དང་བསྡེབས་པ་བཞུགས།།</p>
<a href="https://drupchen.github.io/tsiksum-en/" style="font-family:arial; font-size: 20px;">English</span>

<p style="font-size: 25pt; color: brown;">༈ འགྲེལ་བའི་ལྗགས་ཁྲིད་ཆ་ཚང་བ་བཞི།</p>        
                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་དང་པོ། </p>
          <p style="font-size: 20pt;">  <a href="#tsiksum1">སྒྲ་དང་པོ།</a><span style="font-family:arial; font-size: 20px;">27:38</span> 
                                        <a href="#tsiksum2">སྒྲ་གཉིས་པ།</a><span style="font-family:arial; font-size: 20px;">14:05</span> 
                                        <a href="#tsiksum3">སྒྲ་གསུམ་པའོ།</a><span style="font-family:arial; font-size: 20px;">9:51</span></p>

                <p><p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་གསུམ་པ། </p>
          <p style="font-size: 20pt;">  <a href="#tsiksum4">སྒྲ་དང་པོ།</a><span style="font-family:arial; font-size: 20px;">17:51</span> 
                                        <a href="#tsiksum5">སྒྲ་གཉིས་པ།</a><span style="font-family:arial; font-size: 20px;">17:16</span> 
                                        <a href="#tsiksum6">སྒྲ་གསུམ་པའོ།</a><span style="font-family:arial; font-size: 20px;">11:25</span></p>
                                        
                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་དྲུག་པ། </p>
          <p style="font-size: 20pt;">  <a href="#tsiksum7">སྒྲ་དང་པོ།</a><span style="font-family:arial; font-size: 20px;">2:34</span> 
                                        <a href="#tsiksum8">སྒྲ་གཉིས་པ།</a><span style="font-family:arial; font-size: 20px;">7:51</span> 
                                        <a href="#tsiksum9">སྒྲ་གསུམ་པ།</a><span style="font-family:arial; font-size: 20px;">10:08</span> 
                                        <a href="#tsiksum10">སྒྲ་བཞི་པའོ།</a><span style="font-family:arial; font-size: 20px;">6:46</span></p>
                                        
                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་བཅུ་པ། </p>
          <p style="font-size: 20pt;">  <a href="#tsiksum11">སྒྲ་དང་པོ།</a><span style="font-family:arial; font-size: 20px;">31:52</span> 
                                        <a href="#tsiksum12">སྒྲ་གཉིས་པ།</a><span style="font-family:arial; font-size: 20px;">14:27</span> 
                                        <a href="#tsiksum13">སྒྲ་གསུམ་པ།</a><span style="font-family:arial; font-size: 20px;">4:26</span> 
                                        <a href="#tsiksum14">སྒྲ་བཞི་པ།</a><span style="font-family:arial; font-size: 20px;">9:17</span> 
                                        <a href="#tsiksum15">སྒྲ་ལྔ་པའོ།</a><span style="font-family:arial; font-size: 20px;">6:43</span></p>

<p style="font-size: 25pt; color: brown;">༈ སེང་བྲག་རིན་པོ་ཆེ་ནས་སྒྲ་ཕབ་གནང་བ་མ་བརྩིས་པའི་འགྲེལ་བའི་ལྗགས་ཁྲིད་ཆ་མ་ཚང་བ་ལྔ།</p>                                        
                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་བཞི་པ། </p>
          <p style="font-size: 20pt;">  <a href="#tsiksum16">སྒྲ་དང་པོ།</a><span style="font-family:arial; font-size: 20px;">17:07</span> 
                                        <a href="#tsiksum17">སྒྲ་གཉིས་པ་གནད་དང་པོའི་མཇུག་བར་རོ།</a><span style="font-family:arial; font-size: 20px;">9:00</span></p>
          
                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་བརྒྱད་པ། </p>
          <p style="font-size: 20pt;"><a href="#tsiksum18">གནད་གསུམ་མདོར་བསྟན་པ་ནས་གནད་དང་པོའི་མཇུག་བར་རོ།</a><span style="font-family:arial; font-size: 20px;">40:58</span></p>

                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་བདུན་པ། </p>
          <p style="font-size: 20pt;"><a href="#tsiksum19">གནད་གཉིས་པའི་དཀྱིལ་ནས་མཇུག་བྱང་བར་རོ།</a><span style="font-family:arial; font-size: 20px;">18:50</span></p>

                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་གཉིས་པ། </p>
          <p style="font-size: 20pt;"><a href="#tsiksum20">གནད་གསུམ་པ་དང་མཇུག་དོན་ནོ།</a><span style="font-family:arial; font-size: 20px;">11:10</span></p>

                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་ལྔ་པ། </p>
          <p style="font-size: 20pt;"><a href="#tsiksum21">གནད་གསུམ་པའི་འགོ་ཁོ་ནའོ།</a><span style="font-family:arial; font-size: 20px;">2:19</span></p>

<p style="font-size: 25pt; color: brown;">༈ འགྲེལ་བའི་ཚིག་ལ་མ་གཟིགས་ནས་ལྗགས་ཁྲིད་གནང་བ་གཅིག།</p>
                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་དོན་འགྲེལ། </p>
          <p style="font-size: 20pt;">  <a href="#tsiksum22">སྒྲ་དང་པོ།</a><span style="font-family:arial; font-size: 20px;">15:26</span> 
                                        <a href="#tsiksum23">སྒྲ་གཉིས་པ།</a><span style="font-family:arial; font-size: 20px;">31:00</span> 
                                        <a href="#tsiksum24">སྒྲ་གསུམ་པ།</a><span style="font-family:arial; font-size: 20px;">12:57</span> 
                                        <a href="#tsiksum25">སྒྲ་བཞི་པ།</a><span style="font-family:arial; font-size: 20px;">18:40</span> 
                                        <a href="#tsiksum26">སྒྲ་ལྔ་པ།</a><span style="font-family:arial; font-size: 20px;">14:49</span> 
                                        <a href="#tsiksum27">སྒྲ་དྲུག་པ།</a><span style="font-family:arial; font-size: 20px;">13:44</span> 
                                        <a href="#tsiksum28">སྒྲ་བདུན་པ།</a><span style="font-family:arial; font-size: 20px;">10:28</span> 
                                        <a href="#tsiksum29">སྒྲ་བརྒྱད་པ།</a><span style="font-family:arial; font-size: 20px;">21:30</span> 
                                        <a href="#tsiksum30">སྒྲ་དགུ་པ།</a><span style="font-family:arial; font-size: 20px;">22:28</span> 
                                        <a href="#tsiksum31">སྒྲ་བཅུ་པའོ།</a><span style="font-family:arial; font-size: 20px;">14:45</span></p>

<p style="font-size: 25pt; color: brown;">༈ འགྲེལ་བའི་ཁྲིད་ལུང་གནང་བ་གཉིས།</p>
                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་ལུང་དང་པོ། </p>
          <p style="font-size: 20pt;">  <a href="#tsiksum32">སྒྲ་དང་པོ།</a><span style="font-family:arial; font-size: 20px;">24:53</span> 
                                        <a href="#tsiksum33">སྒྲ་གཉིས་པ།</a><span style="font-family:arial; font-size: 20px;">1:31</span> 
                                        <a href="#tsiksum34">སྒྲ་གསུམ་པ།</a><span style="font-family:arial; font-size: 20px;">10:21</span> 
                                        <a href="#tsiksum35">སྒྲ་བཞི་པ།</a><span style="font-family:arial; font-size: 20px;">8:30</span> 
                                        <a href="#tsiksum36">སྒྲ་ལྔ་པའོ།</a><span style="font-family:arial; font-size: 20px;">6:44</span></p>
                                        
                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་ལུང་གཉིས་པ། </p>
          <p style="font-size: 20pt;"><a href="#tsiksum37">སྒྲ་དང་པོ།</a><span style="font-family:arial; font-size: 20px;">35:02</span> 
                                        <a href="#tsiksum38">སྒྲ་གཉིས་པ།</a><span style="font-family:arial; font-size: 20px;">8:11</span> 
                                        <a href="#tsiksum39">སྒྲ་གསུམ་པ།</a><span style="font-family:arial; font-size: 20px;">8:09</span> 
                                        <a href="#tsiksum40">སྒྲ་བཞི་པའོ།</a><span style="font-family:arial; font-size: 20px;">4:13</span></p>

<p style="font-size: 25pt; color: brown;">༈ རྩ་བའི་ཁྲིད་ལུང་གནང་བ་གཉིས།</p>
                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་རྩ་བའི་ཁྲིད་ལུང་བསྡུས་པ་དང་པོ། </p>
          <p style="font-size: 20pt;">  <a href="#tsiksum41">སྒྲ་གཅིག་པུའོ།</a><span style="font-family:arial; font-size: 20px;">41:18</span></p>
          
                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་རྩ་བའི་ཁྲིད་ལུང་བསྡུས་པ་གཉིས་པ། </p>
          <p style="font-size: 20pt;"><a href="#tsiksum42">སྒྲ་གཅིག་པུའོ།</a><span style="font-family:arial; font-size: 20px;">21:51</span></p>

<p style="font-size: 25pt; color: brown;">༈ རྩ་བའི་ཁྲིད་ལུང་གནད་རེ་རེ་ལ་མདོ་དོན་རེ་རེ་གསུངས་པ་གཅིག།</p>
                <p style="font-size: 20pt;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་རྩ་བ་གནད་རེ་རེའི་མདོ་དོན་ཅན། </p>
          <p style="font-size: 20pt;"><a href="#tsiksum43">སྒྲ་གཅིག་པུའོ།</a><span style="font-family:arial; font-size: 20px;">7:14</span><br></p><br><br><br>
          """)

players = [
        dedent("""\
          <p id="tsiksum1" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་དང་པོ། སྒྲ་དང་པོ།</p>         
          <audio id="hyperplayer1" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_a_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f615f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum2" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་དང་པོ། སྒྲ་གཉིས་པ།</p>         
          <audio id="hyperplayer2" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_a_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f615f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum3" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་དང་པོ། སྒྲ་གསུམ་པའོ།</p>         
          <audio id="hyperplayer3" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_a_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f615f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <audio id="hyperplayer4" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_c_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f635f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
          <p id="tsiksum4" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་གསུམ་པ། སྒྲ་དང་པོ།</p>         
        """),
        dedent("""\
          <p id="tsiksum5" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་གསུམ་པ། སྒྲ་གཉིས་པ།</p>         
          <audio id="hyperplayer5" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_c_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f635f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum6" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་གསུམ་པ། སྒྲ་གསུམ་པའོ།</p>         
          <audio id="hyperplayer6" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_c_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f635f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <audio id="hyperplayer7" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_f_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f665f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
          <p id="tsiksum7" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་དྲུག་པ། སྒྲ་དང་པོ།</p>         
        """),
        dedent("""\
          <p id="tsiksum8" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་དྲུག་པ། སྒྲ་གཉིས་པ།</p>         
          <audio id="hyperplayer8" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_f_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f665f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum9" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་དྲུག་པ། སྒྲ་གསུམ་པ།</p>         
          <audio id="hyperplayer9" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_f_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f665f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum10" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་དྲུག་པ། སྒྲ་བཞི་པའོ།</p>         
          <audio id="hyperplayer10" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_f_4.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f665f342e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum11" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་བཅུ་པ། སྒྲ་དང་པོ།</p>         
          <audio id="hyperplayer11" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_k_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6b5f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum12" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་བཅུ་པ། སྒྲ་གཉིས་པ།</p>         
          <audio id="hyperplayer12" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_k_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6b5f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum13" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་བཅུ་པ། སྒྲ་གསུམ་པ།</p>         
          <audio id="hyperplayer13" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_k_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6b5f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum14" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་བཅུ་པ། སྒྲ་བཞི་པ།</p>         
          <audio id="hyperplayer14" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_k_4.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6b5f342e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum15" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་བཅུ་པ། སྒྲ་ལྔ་པའོ།</p>         
          <audio id="hyperplayer15" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_k_5.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6b5f352e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum16" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་བཞི་པ། སྒྲ་དང་པོ།</p>         
          <audio id="hyperplayer16" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_d_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f645f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum17" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་བཞི་པ། སྒྲ་གཉིས་པ་གནད་དང་པོའི་མཇུག་བར་རོ།</p>         
          <audio id="hyperplayer17" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_d_2_unfinished.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f645f325f756e66696e69736865642e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum18" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་བརྒྱད་པ། གནད་གསུམ་མདོར་བསྟན་པ་ནས་གནད་དང་པོའི་མཇུག་བར་རོ།</p>         
          <audio id="hyperplayer18" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_h_onlybeginning.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f685f6f6e6c79626567696e6e696e672e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum19" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་བདུན་པ། གནད་གཉིས་པའི་དཀྱིལ་ནས་མཇུག་བྱང་བར་རོ།</p>         
          <audio id="hyperplayer19" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_g_nobeginning.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f675f6e6f626567696e6e696e672e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum20" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་གཉིས་པ། གནད་གསུམ་པ་དང་མཇུག་དོན་ནོ།</p>         
          <audio id="hyperplayer20" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_b_onlyend.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f625f6f6e6c79656e642e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum21" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་ལྔ་པ། གནད་གསུམ་པའི་འགོ་ཁོ་ནའོ།</p>         
          <audio id="hyperplayer21" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_e_unfinished.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f655f756e66696e69736865642e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum22" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་དོན་འགྲེལ། སྒྲ་དང་པོ།</p>         
          <audio id="hyperplayer22" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum23" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་དོན་འགྲེལ། སྒྲ་གཉིས་པ།</p>         
          <audio id="hyperplayer23" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum24" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་དོན་འགྲེལ། སྒྲ་གསུམ་པ།</p>         
          <audio id="hyperplayer24" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum25" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་དོན་འགྲེལ། སྒྲ་བཞི་པ།</p>         
          <audio id="hyperplayer25" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_4.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f342e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum26" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་དོན་འགྲེལ། སྒྲ་ལྔ་པ།</p>         
          <audio id="hyperplayer26" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_5.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f352e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum27" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་དོན་འགྲེལ། སྒྲ་དྲུག་པ།</p>         
          <audio id="hyperplayer27" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_6.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f362e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum28" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་དོན་འགྲེལ། སྒྲ་བདུན་པ།</p>         
          <audio id="hyperplayer28" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_7.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f372e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum29" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་དོན་འགྲེལ། སྒྲ་བརྒྱད་པ།</p>         
          <audio id="hyperplayer29" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_8.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f382e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum30" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་དོན་འགྲེལ། སྒྲ་དགུ་པ།</p>         
          <audio id="hyperplayer30" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_9.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f392e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum31" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་དོན་འགྲེལ། སྒྲ་བཅུ་པའོ།</p>         
          <audio id="hyperplayer31" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_l_10.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6c5f31302e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum32" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་ལུང་དང་པོ། སྒྲ་དང་པོ།</p>         
          <audio id="hyperplayer32" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_thrilung_b_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f746872696c756e675f625f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum33" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་ལུང་དང་པོ། སྒྲ་གཉིས་པ།</p>         
          <audio id="hyperplayer33" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_thrilung_b_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f746872696c756e675f625f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum34" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་ལུང་དང་པོ། སྒྲ་གསུམ་པ།</p>         
          <audio id="hyperplayer34" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_thrilung_b_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f746872696c756e675f625f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum35" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་ལུང་དང་པོ། སྒྲ་བཞི་པ།</p>         
          <audio id="hyperplayer35" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_thrilung_b_4.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f746872696c756e675f625f342e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum36" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་ལུང་དང་པོ། སྒྲ་ལྔ་པའོ།</p>         
          <audio id="hyperplayer36" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_thrilung_b_5.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f746872696c756e675f625f352e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum37" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་ལུང་གཉིས་པ། སྒྲ་དང་པོ།</p>         
          <audio id="hyperplayer37" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_j_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6a5f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum38" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་ལུང་གཉིས་པ། སྒྲ་གཉིས་པ།</p>         
          <audio id="hyperplayer38" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_j_2.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6a5f322e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum39" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་ལུང་གཉིས་པ། སྒྲ་གསུམ་པ།</p>         
          <audio id="hyperplayer39" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_j_3.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6a5f332e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum40" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་འགྲེལ་བའི་ཁྲིད་ལུང་གཉིས་པ། སྒྲ་བཞི་པའོ།</p>         
          <audio id="hyperplayer40" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_j_4.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f6a5f342e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum41" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་རྩ་བའི་ཁྲིད་ལུང་བསྡུས་པ་དང་པོ། སྒྲ་གཅིག་པུའོ།</p>         
          <audio id="hyperplayer41" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_commentary_thrilung_a.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f636f6d6d656e746172795f746872696c756e675f612e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum42" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་རྩ་བའི་ཁྲིད་ལུང་བསྡུས་པ་གཉིས་པ། སྒྲ་གཅིག་པུའོ།</p>         
          <audio id="hyperplayer42" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_roottext_thrilung_a_1.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f726f6f74746578745f746872696c756e675f615f312e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
        dedent("""\
          <p id="tsiksum43" style="font-size: 26pt; color: brown;">མཁས་པ་ཤྲཱི་རྒྱལ་པོའི་རྩ་བ་གནད་རེ་རེའི་མདོ་དོན་ཅན། སྒྲ་གཅིག་པུའོ།</p>         
          <audio id="hyperplayer43" style="position:relative; width:97%" src="https://kytsodnangdsm.synology.me:5051/fbdownload/tsiksum_roottext_overview_a.mp3?tid=%22Km_DrqVZqluLxgYF4U4UdJ8q64DcULskdG8b3PY-VbEuoYmpJM1BmBzaljtHil1MaxpbgplWECZhIf71%22&mode=open&dlink=%222f686f6d652f5473696b73756d204e6564656b2070726f6365737365642f7473696b73756d5f726f6f74746578745f6f766572766965775f612e6d7033%22&stdhtml=true&SynoToken=vNiKzAz2rOFeM" type="audio/m4a" controlsList="nodownload" controls></audio>
        """),
]

transcript_start = """\
          <div id="hypertranscript###" class="hyperaudio-transcript" style="resize: vertical; overflow-y:scroll; height:800px; width: 97%; scrollbar-gutter: stable; position:relative; border-style:dashed; border-width: 1px; border-color:#999; padding: 8px">
          <article><section>"""


transcript_end = dedent("""\
          </section></article>
          </div>""")

body_end = dedent("""\
          <script src="https://w.soundcloud.com/player/api.js"></script>
          <script src="js/hyperaudio-lite.js"></script>
          <script src="js/hyperaudio-lite-extension.js"></script>
          <script>
          // minimizedMode is still experimental - it aims to show the current words in the title, which can be seen on the browser tab.
          let minimizedMode = false;
          let autoScroll = true;
          let doubleClick = false;
          let webMonetization = false;
    
          new HyperaudioLite("hypertranscript1", "hyperplayer1", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript2", "hyperplayer2", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript3", "hyperplayer3", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript4", "hyperplayer4", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript5", "hyperplayer5", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript6", "hyperplayer6", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript7", "hyperplayer7", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript8", "hyperplayer8", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript9", "hyperplayer9", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript10", "hyperplayer10", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript11", "hyperplayer11", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript12", "hyperplayer12", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript13", "hyperplayer13", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript14", "hyperplayer14", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript15", "hyperplayer15", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript16", "hyperplayer16", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript17", "hyperplayer17", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript18", "hyperplayer18", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript19", "hyperplayer19", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript20", "hyperplayer20", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript21", "hyperplayer21", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript22", "hyperplayer22", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript23", "hyperplayer23", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript24", "hyperplayer24", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript25", "hyperplayer25", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript26", "hyperplayer26", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript27", "hyperplayer27", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript28", "hyperplayer28", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript29", "hyperplayer29", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript30", "hyperplayer30", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript31", "hyperplayer31", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript32", "hyperplayer32", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript33", "hyperplayer33", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript34", "hyperplayer34", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript35", "hyperplayer35", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript36", "hyperplayer36", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript37", "hyperplayer37", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript38", "hyperplayer38", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript39", "hyperplayer39", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript40", "hyperplayer40", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript41", "hyperplayer41", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript42", "hyperplayer42", minimizedMode, autoScroll, doubleClick, webMonetization);
          new HyperaudioLite("hypertranscript43", "hyperplayer43", minimizedMode, autoScroll, doubleClick, webMonetization);
          </script>
          <script>
            var coll = document.getElementsByClassName("collapsible");
            var i;
            
            for (i = 0; i < coll.length; i++) {
              coll[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var content = this.nextElementSibling;
                if (content.style.display === "block") {
                  content.style.display = "none";
                } else {
                  content.style.display = "block";
                }
              });
            }
          </script>
      </body>
    </html>""")