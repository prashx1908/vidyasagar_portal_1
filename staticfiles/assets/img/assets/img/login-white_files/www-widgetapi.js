(function(){'use strict';var p;function aa(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}}
var r=typeof Object.defineProperties=="function"?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
function ba(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("Cannot find global object");}
var t=ba(this);function u(a,b){if(b)a:{var c=t;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&r(c,a,{configurable:!0,writable:!0,value:b})}}
u("Symbol",function(a){function b(k){if(this instanceof b)throw new TypeError("Symbol is not a constructor");return new c(d+(k||"")+"_"+e++,k)}
function c(k,g){this.g=k;r(this,"description",{configurable:!0,writable:!0,value:g})}
if(a)return a;c.prototype.toString=function(){return this.g};
var d="jscomp_symbol_"+(Math.random()*1E9>>>0)+"_",e=0;return b});
u("Symbol.iterator",function(a){if(a)return a;a=Symbol("Symbol.iterator");for(var b="Array Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array".split(" "),c=0;c<b.length;c++){var d=t[b[c]];typeof d==="function"&&typeof d.prototype[a]!="function"&&r(d.prototype,a,{configurable:!0,writable:!0,value:function(){return ca(aa(this))}})}return a});
function ca(a){a={next:a};a[Symbol.iterator]=function(){return this};
return a}
function v(a){var b=typeof Symbol!="undefined"&&Symbol.iterator&&a[Symbol.iterator];if(b)return b.call(a);if(typeof a.length=="number")return{next:aa(a)};throw Error(String(a)+" is not an iterable or ArrayLike");}
var fa=typeof Object.create=="function"?Object.create:function(a){function b(){}
b.prototype=a;return new b},w;
if(typeof Object.setPrototypeOf=="function")w=Object.setPrototypeOf;else{var x;a:{var ha={a:!0},ia={};try{ia.__proto__=ha;x=ia.a;break a}catch(a){}x=!1}w=x?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var ja=w;
function y(){this.j=!1;this.h=null;this.l=void 0;this.g=1;this.u=this.m=0;this.i=null}
function z(a){if(a.j)throw new TypeError("Generator is already running");a.j=!0}
y.prototype.s=function(a){this.l=a};
function ka(a,b){a.i={P:b,R:!0};a.g=a.m||a.u}
y.prototype.return=function(a){this.i={return:a};this.g=this.u};
function B(a,b,c){a.g=c;return{value:b}}
function la(a){this.g=new y;this.h=a}
function ma(a,b){z(a.g);var c=a.g.h;if(c)return na(a,"return"in c?c["return"]:function(d){return{value:d,done:!0}},b,a.g.return);
a.g.return(b);return C(a)}
function na(a,b,c,d){try{var e=b.call(a.g.h,c);if(!(e instanceof Object))throw new TypeError("Iterator result "+e+" is not an object");if(!e.done)return a.g.j=!1,e;var k=e.value}catch(g){return a.g.h=null,ka(a.g,g),C(a)}a.g.h=null;d.call(a.g,k);return C(a)}
function C(a){for(;a.g.g;)try{var b=a.h(a.g);if(b)return a.g.j=!1,{value:b.value,done:!1}}catch(c){a.g.l=void 0,ka(a.g,c)}a.g.j=!1;if(a.g.i){b=a.g.i;a.g.i=null;if(b.R)throw b.P;return{value:b.return,done:!0}}return{value:void 0,done:!0}}
function oa(a){this.next=function(b){z(a.g);a.g.h?b=na(a,a.g.h.next,b,a.g.s):(a.g.s(b),b=C(a));return b};
this.throw=function(b){z(a.g);a.g.h?b=na(a,a.g.h["throw"],b,a.g.s):(ka(a.g,b),b=C(a));return b};
this.return=function(b){return ma(a,b)};
this[Symbol.iterator]=function(){return this}}
function pa(a){function b(d){return a.next(d)}
function c(d){return a.throw(d)}
return new Promise(function(d,e){function k(g){g.done?d(g.value):Promise.resolve(g.value).then(b,c).then(k,e)}
k(a.next())})}
function qa(a){return pa(new oa(new la(a)))}
u("Promise",function(a){function b(g){this.h=0;this.i=void 0;this.g=[];this.s=!1;var f=this.j();try{g(f.resolve,f.reject)}catch(h){f.reject(h)}}
function c(){this.g=null}
function d(g){return g instanceof b?g:new b(function(f){f(g)})}
if(a)return a;c.prototype.h=function(g){if(this.g==null){this.g=[];var f=this;this.i(function(){f.l()})}this.g.push(g)};
var e=t.setTimeout;c.prototype.i=function(g){e(g,0)};
c.prototype.l=function(){for(;this.g&&this.g.length;){var g=this.g;this.g=[];for(var f=0;f<g.length;++f){var h=g[f];g[f]=null;try{h()}catch(l){this.j(l)}}}this.g=null};
c.prototype.j=function(g){this.i(function(){throw g;})};
b.prototype.j=function(){function g(l){return function(m){h||(h=!0,l.call(f,m))}}
var f=this,h=!1;return{resolve:g(this.K),reject:g(this.l)}};
b.prototype.K=function(g){if(g===this)this.l(new TypeError("A Promise cannot resolve to itself"));else if(g instanceof b)this.M(g);else{a:switch(typeof g){case "object":var f=g!=null;break a;case "function":f=!0;break a;default:f=!1}f?this.J(g):this.m(g)}};
b.prototype.J=function(g){var f=void 0;try{f=g.then}catch(h){this.l(h);return}typeof f=="function"?this.N(f,g):this.m(g)};
b.prototype.l=function(g){this.u(2,g)};
b.prototype.m=function(g){this.u(1,g)};
b.prototype.u=function(g,f){if(this.h!=0)throw Error("Cannot settle("+g+", "+f+"): Promise already settled in state"+this.h);this.h=g;this.i=f;this.h===2&&this.L();this.B()};
b.prototype.L=function(){var g=this;e(function(){if(g.T()){var f=t.console;typeof f!=="undefined"&&f.error(g.i)}},1)};
b.prototype.T=function(){if(this.s)return!1;var g=t.CustomEvent,f=t.Event,h=t.dispatchEvent;if(typeof h==="undefined")return!0;typeof g==="function"?g=new g("unhandledrejection",{cancelable:!0}):typeof f==="function"?g=new f("unhandledrejection",{cancelable:!0}):(g=t.document.createEvent("CustomEvent"),g.initCustomEvent("unhandledrejection",!1,!0,g));g.promise=this;g.reason=this.i;return h(g)};
b.prototype.B=function(){if(this.g!=null){for(var g=0;g<this.g.length;++g)k.h(this.g[g]);this.g=null}};
var k=new c;b.prototype.M=function(g){var f=this.j();g.A(f.resolve,f.reject)};
b.prototype.N=function(g,f){var h=this.j();try{g.call(f,h.resolve,h.reject)}catch(l){h.reject(l)}};
b.prototype.then=function(g,f){function h(q,A){return typeof q=="function"?function(da){try{l(q(da))}catch(ea){m(ea)}}:A}
var l,m,n=new b(function(q,A){l=q;m=A});
this.A(h(g,l),h(f,m));return n};
b.prototype.catch=function(g){return this.then(void 0,g)};
b.prototype.A=function(g,f){function h(){switch(l.h){case 1:g(l.i);break;case 2:f(l.i);break;default:throw Error("Unexpected state: "+l.h);}}
var l=this;this.g==null?k.h(h):this.g.push(h);this.s=!0};
b.resolve=d;b.reject=function(g){return new b(function(f,h){h(g)})};
b.race=function(g){return new b(function(f,h){for(var l=v(g),m=l.next();!m.done;m=l.next())d(m.value).A(f,h)})};
b.all=function(g){var f=v(g),h=f.next();return h.done?d([]):new b(function(l,m){function n(da){return function(ea){q[da]=ea;A--;A==0&&l(q)}}
var q=[],A=0;do q.push(void 0),A++,d(h.value).A(n(q.length-1),m),h=f.next();while(!h.done)})};
return b});
function D(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
var ra=typeof Object.assign=="function"?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)D(d,e)&&(a[e]=d[e])}return a};
u("Object.assign",function(a){return a||ra});
u("Symbol.dispose",function(a){return a?a:Symbol("Symbol.dispose")});
u("WeakMap",function(a){function b(h){this.g=(f+=Math.random()+1).toString();if(h){h=v(h);for(var l;!(l=h.next()).done;)l=l.value,this.set(l[0],l[1])}}
function c(){}
function d(h){var l=typeof h;return l==="object"&&h!==null||l==="function"}
function e(h){if(!D(h,g)){var l=new c;r(h,g,{value:l})}}
function k(h){var l=Object[h];l&&(Object[h]=function(m){if(m instanceof c)return m;Object.isExtensible(m)&&e(m);return l(m)})}
if(function(){if(!a||!Object.seal)return!1;try{var h=Object.seal({}),l=Object.seal({}),m=new a([[h,2],[l,3]]);if(m.get(h)!=2||m.get(l)!=3)return!1;m.delete(h);m.set(l,4);return!m.has(h)&&m.get(l)==4}catch(n){return!1}}())return a;
var g="$jscomp_hidden_"+Math.random();k("freeze");k("preventExtensions");k("seal");var f=0;b.prototype.set=function(h,l){if(!d(h))throw Error("Invalid WeakMap key");e(h);if(!D(h,g))throw Error("WeakMap key fail: "+h);h[g][this.g]=l;return this};
b.prototype.get=function(h){return d(h)&&D(h,g)?h[g][this.g]:void 0};
b.prototype.has=function(h){return d(h)&&D(h,g)&&D(h[g],this.g)};
b.prototype.delete=function(h){return d(h)&&D(h,g)&&D(h[g],this.g)?delete h[g][this.g]:!1};
return b});
u("Map",function(a){function b(){var f={};return f.previous=f.next=f.head=f}
function c(f,h){var l=f[1];return ca(function(){if(l){for(;l.head!=f[1];)l=l.previous;for(;l.next!=l.head;)return l=l.next,{done:!1,value:h(l)};l=null}return{done:!0,value:void 0}})}
function d(f,h){var l=h&&typeof h;l=="object"||l=="function"?k.has(h)?l=k.get(h):(l=""+ ++g,k.set(h,l)):l="p_"+h;var m=f[0][l];if(m&&D(f[0],l))for(f=0;f<m.length;f++){var n=m[f];if(h!==h&&n.key!==n.key||h===n.key)return{id:l,list:m,index:f,o:n}}return{id:l,list:m,index:-1,o:void 0}}
function e(f){this[0]={};this[1]=b();this.size=0;if(f){f=v(f);for(var h;!(h=f.next()).done;)h=h.value,this.set(h[0],h[1])}}
if(function(){if(!a||typeof a!="function"||!a.prototype.entries||typeof Object.seal!="function")return!1;try{var f=Object.seal({x:4}),h=new a(v([[f,"s"]]));if(h.get(f)!="s"||h.size!=1||h.get({x:4})||h.set({x:4},"t")!=h||h.size!=2)return!1;var l=h.entries(),m=l.next();if(m.done||m.value[0]!=f||m.value[1]!="s")return!1;m=l.next();return m.done||m.value[0].x!=4||m.value[1]!="t"||!l.next().done?!1:!0}catch(n){return!1}}())return a;
var k=new WeakMap;e.prototype.set=function(f,h){f=f===0?0:f;var l=d(this,f);l.list||(l.list=this[0][l.id]=[]);l.o?l.o.value=h:(l.o={next:this[1],previous:this[1].previous,head:this[1],key:f,value:h},l.list.push(l.o),this[1].previous.next=l.o,this[1].previous=l.o,this.size++);return this};
e.prototype.delete=function(f){f=d(this,f);return f.o&&f.list?(f.list.splice(f.index,1),f.list.length||delete this[0][f.id],f.o.previous.next=f.o.next,f.o.next.previous=f.o.previous,f.o.head=null,this.size--,!0):!1};
e.prototype.clear=function(){this[0]={};this[1]=this[1].previous=b();this.size=0};
e.prototype.has=function(f){return!!d(this,f).o};
e.prototype.get=function(f){return(f=d(this,f).o)&&f.value};
e.prototype.entries=function(){return c(this,function(f){return[f.key,f.value]})};
e.prototype.keys=function(){return c(this,function(f){return f.key})};
e.prototype.values=function(){return c(this,function(f){return f.value})};
e.prototype.forEach=function(f,h){for(var l=this.entries(),m;!(m=l.next()).done;)m=m.value,f.call(h,m[1],m[0],this)};
e.prototype[Symbol.iterator]=e.prototype.entries;var g=0;return e});
u("Array.prototype.find",function(a){return a?a:function(b,c){a:{var d=this;d instanceof String&&(d=String(d));for(var e=d.length,k=0;k<e;k++){var g=d[k];if(b.call(c,g,k,d)){b=g;break a}}b=void 0}return b}});
u("Set",function(a){function b(c){this.g=new Map;if(c){c=v(c);for(var d;!(d=c.next()).done;)this.add(d.value)}this.size=this.g.size}
if(function(){if(!a||typeof a!="function"||!a.prototype.entries||typeof Object.seal!="function")return!1;try{var c=Object.seal({x:4}),d=new a(v([c]));if(!d.has(c)||d.size!=1||d.add(c)!=d||d.size!=1||d.add({x:4})!=d||d.size!=2)return!1;var e=d.entries(),k=e.next();if(k.done||k.value[0]!=c||k.value[1]!=c)return!1;k=e.next();return k.done||k.value[0]==c||k.value[0].x!=4||k.value[1]!=k.value[0]?!1:e.next().done}catch(g){return!1}}())return a;
b.prototype.add=function(c){c=c===0?0:c;this.g.set(c,c);this.size=this.g.size;return this};
b.prototype.delete=function(c){c=this.g.delete(c);this.size=this.g.size;return c};
b.prototype.clear=function(){this.g.clear();this.size=0};
b.prototype.has=function(c){return this.g.has(c)};
b.prototype.entries=function(){return this.g.entries()};
b.prototype.values=function(){return this.g.values()};
b.prototype.keys=b.prototype.values;b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(c,d){var e=this;this.g.forEach(function(k){return c.call(d,k,k,e)})};
return b});/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var E=this||self;function F(a){var b=typeof a;return b=="object"&&a!=null||b=="function"}
function sa(a){return Object.prototype.hasOwnProperty.call(a,ta)&&a[ta]||(a[ta]=++ua)}
var ta="closure_uid_"+(Math.random()*1E9>>>0),ua=0;function va(a,b,c){return a.call.apply(a.bind,arguments)}
function wa(a,b,c){if(!a)throw Error();if(arguments.length>2){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}}
function G(a,b,c){G=Function.prototype.bind&&Function.prototype.bind.toString().indexOf("native code")!=-1?va:wa;return G.apply(null,arguments)}
function H(a,b){a=a.split(".");var c=E;a[0]in c||typeof c.execScript=="undefined"||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b}
function xa(a,b){function c(){}
c.prototype=b.prototype;a.I=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.Y=function(d,e,k){for(var g=Array(arguments.length-2),f=2;f<arguments.length;f++)g[f-2]=arguments[f];return b.prototype[e].apply(d,g)}}
;var ya=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if(typeof a==="string")return typeof b!=="string"||b.length!=1?-1:a.indexOf(b,0);
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},I=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=typeof a==="string"?a.split(""):a,k=0;k<d;k++)k in e&&b.call(c,e[k],k,a)};
function za(a,b){b=ya(a,b);b>=0&&Array.prototype.splice.call(a,b,1)}
function Aa(a){return Array.prototype.concat.apply([],arguments)}
function Ba(a){var b=a.length;if(b>0){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
;function Ca(a,b){this.i=a;this.j=b;this.h=0;this.g=null}
Ca.prototype.get=function(){if(this.h>0){this.h--;var a=this.g;this.g=a.next;a.next=null}else a=this.i();return a};var Da,J;a:{for(var Ea=["CLOSURE_FLAGS"],K=E,Fa=0;Fa<Ea.length;Fa++)if(K=K[Ea[Fa]],K==null){J=null;break a}J=K}var Ga=J&&J[610401301];Da=Ga!=null?Ga:!1;var Ha=/&/g,Ia=/</g,Ja=/>/g,Ka=/"/g,La=/'/g,Ma=/\x00/g,Na=/[\x00&<>"']/;function Oa(){var a=E.navigator;return a&&(a=a.userAgent)?a:""}
var L,Pa=E.navigator;L=Pa?Pa.userAgentData||null:null;function Qa(){return Da?L?L.brands.some(function(a){return(a=a.brand)&&a.indexOf("Chromium")!=-1}):!1:!1}
function M(a){return Oa().indexOf(a)!=-1}
;function Ra(){return Da?!!L&&L.brands.length>0:!1}
function Sa(a){var b={};a.forEach(function(c){b[c[0]]=c[1]});
return function(c){return b[c.find(function(d){return d in b})]||""}}
function Ta(){for(var a=Oa(),b=RegExp("([A-Z][\\w ]+)/([^\\s]+)\\s*(?:\\((.*?)\\))?","g"),c=[],d;d=b.exec(a);)c.push([d[1],d[2],d[3]||void 0]);a=Sa(c);return(Ra()?Qa():(M("Chrome")||M("CriOS"))&&(Ra()||!M("Edge"))||M("Silk"))?a(["Chrome","CriOS","HeadlessChrome"]):""}
function Ua(){if(Ra()){var a=L.brands.find(function(b){return b.brand==="Chromium"});
if(!a||!a.version)return NaN;a=a.version.split(".")}else{a=Ta();if(a==="")return NaN;a=a.split(".")}return a.length===0?NaN:Number(a[0])}
;/*

 SPDX-License-Identifier: Apache-2.0
*/
function N(a){this.g=a}
N.prototype.toString=function(){return this.g};
var Va=new N("about:invalid#zClosurez");function Wa(a){this.S=a}
function O(a){return new Wa(function(b){return b.substr(0,a.length+1).toLowerCase()===a+":"})}
var Xa=[O("data"),O("http"),O("https"),O("mailto"),O("ftp"),new Wa(function(a){return/^[^:]*([/?#]|$)/.test(a)})];
function Ya(a){var b=b===void 0?Xa:b;a:if(b=b===void 0?Xa:b,!(a instanceof N)){for(var c=0;c<b.length;++c){var d=b[c];if(d instanceof Wa&&d.S(a)){a=new N(a);break a}}a=void 0}return a||Va}
var Za=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var $a={X:0,V:1,W:2,0:"FORMATTED_HTML_CONTENT",1:"EMBEDDED_INTERNAL_CONTENT",2:"EMBEDDED_TRUSTED_EXTERNAL_CONTENT"};function P(a,b){b=Error.call(this,a+" cannot be used with intent "+$a[b]);this.message=b.message;"stack"in b&&(this.stack=b.stack);this.type=a;this.name="TypeCannotBeUsedWithIntentError"}
var Q=Error;P.prototype=fa(Q.prototype);P.prototype.constructor=P;if(ja)ja(P,Q);else for(var R in Q)if(R!="prototype")if(Object.defineProperties){var ab=Object.getOwnPropertyDescriptor(Q,R);ab&&Object.defineProperty(P,R,ab)}else P[R]=Q[R];P.I=Q.prototype;
function bb(a,b){a.removeAttribute("srcdoc");var c="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-storage-access-by-user-activation".split(" ");a.setAttribute("sandbox","");for(var d=0;d<c.length;d++)a.sandbox.supports&&!a.sandbox.supports(c[d])||a.sandbox.add(c[d]);if(b instanceof N)if(b instanceof N)b=b.g;else throw Error("");else b=Za.test(b)?b:void 0;b!==void 0&&(a.src=b)}
;function cb(a){Na.test(a)&&(a.indexOf("&")!=-1&&(a=a.replace(Ha,"&amp;")),a.indexOf("<")!=-1&&(a=a.replace(Ia,"&lt;")),a.indexOf(">")!=-1&&(a=a.replace(Ja,"&gt;")),a.indexOf('"')!=-1&&(a=a.replace(Ka,"&quot;")),a.indexOf("'")!=-1&&(a=a.replace(La,"&#39;")),a.indexOf("\x00")!=-1&&(a=a.replace(Ma,"&#0;")));return a}
;function db(){var a=document;var b="IFRAME";a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)}
;var eb;function fb(){var a=E.MessageChannel;typeof a==="undefined"&&typeof window!=="undefined"&&window.postMessage&&window.addEventListener&&!M("Presto")&&(a=function(){var e=db();e.style.display="none";document.documentElement.appendChild(e);var k=e.contentWindow;e=k.document;e.open();e.close();var g="callImmediate"+Math.random(),f=k.location.protocol=="file:"?"*":k.location.protocol+"//"+k.location.host;e=G(function(h){if((f=="*"||h.origin==f)&&h.data==g)this.port1.onmessage()},this);
k.addEventListener("message",e,!1);this.port1={};this.port2={postMessage:function(){k.postMessage(g,f)}}});
if(typeof a!=="undefined"){var b=new a,c={},d=c;b.port1.onmessage=function(){if(c.next!==void 0){c=c.next;var e=c.F;c.F=null;e()}};
return function(e){d.next={F:e};d=d.next;b.port2.postMessage(0)}}return function(e){E.setTimeout(e,0)}}
;function gb(a){E.setTimeout(function(){throw a;},0)}
;function hb(){this.h=this.g=null}
hb.prototype.add=function(a,b){var c=ib.get();c.set(a,b);this.h?this.h.next=c:this.g=c;this.h=c};
hb.prototype.remove=function(){var a=null;this.g&&(a=this.g,this.g=this.g.next,this.g||(this.h=null),a.next=null);return a};
var ib=new Ca(function(){return new jb},function(a){return a.reset()});
function jb(){this.next=this.scope=this.g=null}
jb.prototype.set=function(a,b){this.g=a;this.scope=b;this.next=null};
jb.prototype.reset=function(){this.next=this.scope=this.g=null};var S,kb=!1,lb=new hb;function mb(a){S||nb();kb||(S(),kb=!0);lb.add(a,void 0)}
function nb(){if(E.Promise&&E.Promise.resolve){var a=E.Promise.resolve(void 0);S=function(){a.then(ob)}}else S=function(){var b=ob;
typeof E.setImmediate!=="function"||E.Window&&E.Window.prototype&&E.Window.prototype.setImmediate==E.setImmediate?(eb||(eb=fb()),eb(b)):E.setImmediate(b)}}
function ob(){for(var a;a=lb.remove();){try{a.g.call(a.scope)}catch(c){gb(c)}var b=ib;b.j(a);b.h<100&&(b.h++,a.next=b.g,b.g=a)}kb=!1}
;function T(){this.i=this.i;this.j=this.j}
T.prototype.i=!1;T.prototype.dispose=function(){this.i||(this.i=!0,this.C())};
T.prototype.addOnDisposeCallback=function(a,b){this.i?b!==void 0?a.call(b):a():(this.j||(this.j=[]),this.j.push(b!==void 0?G(a,b):a))};
T.prototype.C=function(){if(this.j)for(;this.j.length;)this.j.shift()()};function U(a){T.call(this);this.s=1;this.l=[];this.m=0;this.g=[];this.h={};this.u=!!a}
xa(U,T);p=U.prototype;p.subscribe=function(a,b,c){var d=this.h[a];d||(d=this.h[a]=[]);var e=this.s;this.g[e]=a;this.g[e+1]=b;this.g[e+2]=c;this.s=e+3;d.push(e);return e};
function pb(a,b,c){var d=V;if(a=d.h[a]){var e=d.g;(a=a.find(function(k){return e[k+1]==b&&e[k+2]==c}))&&d.D(a)}}
p.D=function(a){var b=this.g[a];if(b){var c=this.h[b];this.m!=0?(this.l.push(a),this.g[a+1]=function(){}):(c&&za(c,a),delete this.g[a],delete this.g[a+1],delete this.g[a+2])}return!!b};
p.H=function(a,b){var c=this.h[a];if(c){for(var d=Array(arguments.length-1),e=1,k=arguments.length;e<k;e++)d[e-1]=arguments[e];if(this.u)for(e=0;e<c.length;e++){var g=c[e];qb(this.g[g+1],this.g[g+2],d)}else{this.m++;try{for(e=0,k=c.length;e<k&&!this.i;e++)g=c[e],this.g[g+1].apply(this.g[g+2],d)}finally{if(this.m--,this.l.length>0&&this.m==0)for(;c=this.l.pop();)this.D(c)}}return e!=0}return!1};
function qb(a,b,c){mb(function(){a.apply(b,c)})}
p.clear=function(a){if(a){var b=this.h[a];b&&(b.forEach(this.D,this),delete this.h[a])}else this.g.length=0,this.h={}};
p.C=function(){U.I.C.call(this);this.clear();this.l.length=0};var rb=RegExp("^(?:([^:/?#.]+):)?(?://(?:([^\\\\/?#]*)@)?([^\\\\/?#]*?)(?::([0-9]+))?(?=[\\\\/?#]|$))?([^?#]+)?(?:\\?([^#]*))?(?:#([\\s\\S]*))?$");function sb(a){var b=a.match(rb);a=b[1];var c=b[2],d=b[3];b=b[4];var e="";a&&(e+=a+":");d&&(e+="//",c&&(e+=c+"@"),e+=d,b&&(e+=":"+b));return e}
function tb(a,b,c){if(Array.isArray(b))for(var d=0;d<b.length;d++)tb(a,String(b[d]),c);else b!=null&&c.push(a+(b===""?"":"="+encodeURIComponent(String(b))))}
function ub(a){var b=[],c;for(c in a)tb(c,a[c],b);return b.join("&")}
var vb=/#|$/;var wb=["https://www.google.com"];function xb(){var a=this;this.g=[];this.h=function(){Promise.all(a.g.map(function(b){document.requestStorageAccessFor(b)})).then(function(){window.removeEventListener("click",a.h)})}}
function yb(){var a;return qa(function(b){if(b.g==1)return(a=document.hasStorageAccess)?b=B(b,document.hasStorageAccess(),3):(b.g=2,b=void 0),b;b.g!=2&&(a=b.l);if(a)b=b.return(!1);else{var c=b.return;var d=Ua()>=119;b=c.call(b,d&&!!navigator.permissions&&!!navigator.permissions.query&&"requestStorageAccessFor"in document)}return b})}
function zb(){var a=new xb,b=["https://www.youtube.com"];b=b===void 0?wb:b;qa(function(c){switch(c.g){case 1:return B(c,yb(),2);case 2:if(!c.l){c.g=3;break}return B(c,Promise.all(b.map(function(d){var e;return qa(function(k){if(k.g==1)return k.m=2,B(k,navigator.permissions.query({name:"top-level-storage-access",requestedOrigin:d}),4);k.g!=2?(e=k.l,e.state==="prompt"&&a.g.push(d),k.g=0,k.m=0):(k.m=0,k.i=null,k.g=0)})})),4);
case 4:a.g.length>0&&window.addEventListener("click",a.h);case 3:return c.return()}})}
;var W={},Ab=[],V=new U,Bb={};function Cb(){for(var a=v(Ab),b=a.next();!b.done;b=a.next())b=b.value,b()}
function Db(a,b){return a.tagName.toLowerCase().substring(0,3)==="yt:"?a.getAttribute(b):a.dataset?a.dataset[b]:a.getAttribute("data-"+b)}
function Eb(a){V.H.apply(V,arguments)}
;function Fb(a){this.g=a||{};a=[this.g,window.YTConfig||{}];for(var b=0;b<a.length;b++)a[b].host&&(a[b].host=a[b].host.toString().replace("http://","https://"))}
function X(a,b){a=[a.g,window.YTConfig||{}];for(var c=0;c<a.length;c++){var d=a[c][b];if(d!==void 0)return d}return null}
function Gb(a,b,c){Y||(Y={},Hb=new Set,Ib.addEventListener("message",function(d){a:if(Hb.has(d.origin)){try{var e=JSON.parse(d.data)}catch(f){break a}var k=Y[e.id];if(k&&d.origin===k.O)switch(d=k.U,d.s=!0,d.s&&(I(d.m,d.sendMessage,d),d.m.length=0),k=e.event,e=e.info,k){case "apiInfoDelivery":if(F(e))for(var g in e)e.hasOwnProperty(g)&&(d.v[g]=e[g]);break;case "infoDelivery":Jb(d,e);break;case "initialDelivery":F(e)&&(clearInterval(d.i),d.playerInfo={},d.v={},Kb(d,e.apiInterface),Jb(d,e));break;default:d.j.i||
(g={target:d,data:e},d.j.H(k,g),Eb("player."+k,g))}}}));
a=String(X(a,"host"));Y[c]={U:b,O:a};Hb.add(a)}
var Y=null,Hb=null,Ib=window;function Lb(a){return(a.search("cue")===0||a.search("load")===0)&&a!=="loadModule"}
function Mb(a){return a.search("get")===0||a.search("is")===0}
;var Nb=window;
function Z(a,b){this.v={};this.playerInfo={};this.videoTitle="";this.l=this.g=this.h=null;this.i=0;this.s=!1;this.m=[];this.j=null;this.B={};if(!a)throw Error("YouTube player element ID required.");this.id=sa(this);b=Object.assign({title:"video player",videoId:"",width:640,height:360},b||{});var c=document;if(a=typeof a==="string"?c.getElementById(a):a)if(Nb.yt_embedsEnableRsaforFromIframeApi&&zb(),c=a.tagName.toLowerCase()==="iframe",b.host||(b.host=c?sb(a.src):"https://www.youtube.com"),this.h=
new Fb(b),c||(b=Ob(this,a),this.l=a,(c=a.parentNode)&&c.replaceChild(b,a),a=b),this.g=a,this.g.id||(this.g.id="widget"+sa(this.g)),W[this.g.id]=this,window.postMessage){this.j=new U;Pb(this);b=X(this.h,"events");for(var d in b)b.hasOwnProperty(d)&&this.addEventListener(d,b[d]);for(var e in Bb)Bb.hasOwnProperty(e)&&Qb(this,e)}}
p=Z.prototype;p.setSize=function(a,b){this.g.width=a.toString();this.g.height=b.toString();return this};
p.getIframe=function(){return this.g};
p.addEventListener=function(a,b){var c=b;typeof b==="string"&&(c=function(){window[b].apply(window,arguments)});
if(!c)return this;this.j.subscribe(a,c);Rb(this,a);return this};
function Qb(a,b){b=b.split(".");if(b.length===2){var c=b[1];"player"===b[0]&&Rb(a,c)}}
p.destroy=function(){this.g&&this.g.id&&(W[this.g.id]=null);var a=this.j;a&&typeof a.dispose=="function"&&a.dispose();if(this.l){a=this.l;var b=this.g,c=b.parentNode;c&&c.replaceChild(a,b)}else(a=this.g)&&a.parentNode&&a.parentNode.removeChild(a);Y&&(Y[this.id]=null);this.h=null;this.g&&this.u&&this.g.removeEventListener("load",this.u);this.l=this.g=null};
function Sb(a,b,c){c=c||[];c=Array.prototype.slice.call(c);b={event:"command",func:b,args:c};a.s?a.sendMessage(b):a.m.push(b)}
function Ob(a,b){var c=document.createElement("iframe");b=b.attributes;for(var d=0,e=b.length;d<e;d++){var k=b[d].value;k!=null&&k!==""&&k!=="null"&&c.setAttribute(b[d].name,k)}c.setAttribute("frameBorder","0");c.setAttribute("allowfullscreen","");c.setAttribute("allow","accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share");c.setAttribute("referrerPolicy","strict-origin-when-cross-origin");c.setAttribute("title","YouTube "+X(a.h,"title"));(b=X(a.h,"width"))&&
c.setAttribute("width",b.toString());(b=X(a.h,"height"))&&c.setAttribute("height",b.toString());var g=Tb(a);g.enablejsapi=window.postMessage?1:0;window.location.host&&(g.origin=window.location.protocol+"//"+window.location.host);g.widgetid=a.id;window.location.href&&I(["debugjs","debugcss"],function(f){var h=window.location.href;var l=h.search(vb);b:{var m=0;for(var n=f.length;(m=h.indexOf(f,m))>=0&&m<l;){var q=h.charCodeAt(m-1);if(q==38||q==63)if(q=h.charCodeAt(m+n),!q||q==61||q==38||q==35)break b;
m+=n+1}m=-1}if(m<0)h=null;else{n=h.indexOf("&",m);if(n<0||n>l)n=l;m+=f.length+1;h=decodeURIComponent(h.slice(m,n!==-1?n:0).replace(/\+/g," "))}h!==null&&(g[f]=h)});
a=""+X(a.h,"host")+("/embed/"+X(a.h,"videoId"))+"?"+ub(g);Nb.yt_embedsEnableIframeSrcWithIntent?(bb(c,Ya(a)),c.sandbox.add("allow-presentation","allow-top-navigation")):c.src=a;return c}
p.G=function(){this.g&&this.g.contentWindow?this.sendMessage({event:"listening"}):clearInterval(this.i)};
function Pb(a){Gb(a.h,a,a.id);a.i=setInterval(a.G.bind(a),250);a.g&&(a.u=function(){clearInterval(a.i);a.i=setInterval(a.G.bind(a),250)},a.g.addEventListener("load",a.u))}
function Rb(a,b){a.B[b]||(a.B[b]=!0,Sb(a,"addEventListener",[b]))}
p.sendMessage=function(a){a.id=this.id;a.channel="widget";a=JSON.stringify(a);var b=[sb(this.g.src||"").replace("http:","https:")];if(this.g.contentWindow)for(var c=0;c<b.length;c++)try{this.g.contentWindow.postMessage(a,b[c])}catch(d){if(d.name&&d.name==="SyntaxError")d.message&&d.message.indexOf("target origin ''")>0||console&&console.warn&&console.warn(d);else throw d;}else console&&console.warn&&console.warn("The YouTube player is not attached to the DOM. API calls should be made after the onReady event. See more: https://developers.google.com/youtube/iframe_api_reference#Events")};
function Tb(a){var b=X(a.h,"playerVars");if(b){var c={},d;for(d in b)c[d]=b[d];b=c}else b={};window!==window.top&&document.referrer&&(b.widget_referrer=document.referrer.substring(0,256));if(a=X(a.h,"embedConfig")){if(F(a))try{a=JSON.stringify(a)}catch(e){console.error("Invalid embed config JSON",e)}b.embed_config=a}return b}
function Jb(a,b){if(F(b)){for(var c in b)b.hasOwnProperty(c)&&(a.playerInfo[c]=b[c]);a.playerInfo.hasOwnProperty("videoData")&&(b=a.playerInfo.videoData,b.hasOwnProperty("title")&&b.title?(b=b.title,b!==a.videoTitle&&(a.videoTitle=b,a.g.setAttribute("title",b))):(a.videoTitle="",a.g.setAttribute("title","YouTube "+X(a.h,"title"))))}}
function Kb(a,b){I(b,function(c){this[c]||(c==="getCurrentTime"?this[c]=function(){var d=this.playerInfo.currentTime;if(this.playerInfo.playerState===1){var e=(Date.now()/1E3-this.playerInfo.currentTimeLastUpdated_)*this.playerInfo.playbackRate;e>0&&(d+=Math.min(e,1))}return d}:Lb(c)?this[c]=function(){this.playerInfo={};
this.v={};Sb(this,c,arguments);return this}:Mb(c)?this[c]=function(){var d=0;
c.search("get")===0?d=3:c.search("is")===0&&(d=2);return this.playerInfo[c.charAt(d).toLowerCase()+c.substr(d+1)]}:this[c]=function(){Sb(this,c,arguments);
return this})},a)}
p.getVideoEmbedCode=function(){var a=X(this.h,"host")+("/embed/"+X(this.h,"videoId")),b=Number(X(this.h,"width")),c=Number(X(this.h,"height"));if(isNaN(b)||isNaN(c))throw Error("Invalid width or height property");b=Math.floor(b);c=Math.floor(c);var d=this.videoTitle;a=cb(a);d=cb(d!=null?d:"YouTube video player");return'<iframe width="'+b+'" height="'+c+'" src="'+a+'" title="'+(d+'" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>')};
p.getOptions=function(a){return this.v.namespaces?a?this.v[a]?this.v[a].options||[]:[]:this.v.namespaces||[]:[]};
p.getOption=function(a,b){if(this.v.namespaces&&a&&b&&this.v[a])return this.v[a][b]};
function Ub(a){if(a.tagName.toLowerCase()!=="iframe"){var b=Db(a,"videoid");b&&(b={videoId:b,width:Db(a,"width"),height:Db(a,"height")},new Z(a,b))}}
;H("YT.PlayerState.UNSTARTED",-1);H("YT.PlayerState.ENDED",0);H("YT.PlayerState.PLAYING",1);H("YT.PlayerState.PAUSED",2);H("YT.PlayerState.BUFFERING",3);H("YT.PlayerState.CUED",5);H("YT.get",function(a){return W[a]});
H("YT.scan",Cb);H("YT.subscribe",function(a,b,c){V.subscribe(a,b,c);Bb[a]=!0;for(var d in W)W.hasOwnProperty(d)&&Qb(W[d],a)});
H("YT.unsubscribe",function(a,b,c){pb(a,b,c)});
H("YT.Player",Z);Z.prototype.destroy=Z.prototype.destroy;Z.prototype.setSize=Z.prototype.setSize;Z.prototype.getIframe=Z.prototype.getIframe;Z.prototype.addEventListener=Z.prototype.addEventListener;Z.prototype.getVideoEmbedCode=Z.prototype.getVideoEmbedCode;Z.prototype.getOptions=Z.prototype.getOptions;Z.prototype.getOption=Z.prototype.getOption;
Ab.push(function(a){var b=a;b||(b=document);a=Ba(b.getElementsByTagName("yt:player"));var c=b||document;if(c.querySelectorAll&&c.querySelector)b=c.querySelectorAll(".yt-player");else{var d;c=document;b=b||c;if(b.querySelectorAll&&b.querySelector)b=b.querySelectorAll(".yt-player");else if(b.getElementsByClassName){var e=b.getElementsByClassName("yt-player");b=e}else{e=b.getElementsByTagName("*");var k={};for(c=d=0;b=e[c];c++){var g=b.className,f;if(f=typeof g.split=="function")f=ya(g.split(/\s+/),
"yt-player")>=0;f&&(k[d++]=b)}k.length=d;b=k}}b=Ba(b);I(Aa(a,b),Ub)});
typeof YTConfig!=="undefined"&&YTConfig.parsetags&&YTConfig.parsetags!=="onload"||Cb();var Vb=E.onYTReady;Vb&&Vb();var Wb=E.onYouTubeIframeAPIReady;Wb&&Wb();var Xb=E.onYouTubePlayerAPIReady;Xb&&Xb();}).call(this);
