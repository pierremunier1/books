(window.webpackJsonp=window.webpackJsonp||[]).push([[18],{1063:function(e,t,r){"use strict";var n=r(446);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var a=n(r(2)),o=(0,n(r(451)).default)(a.default.createElement("path",{d:"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"}),"Assessment");t.default=o},1382:function(e,t,r){"use strict";t.a={ARROW_RIGHT:"arrow-right",ASSESSMENT:"assessment",BELL:"bell",CHECK:"check",CHEVRON_DOWN:"chevron-down",CHEVRON_LEFT:"chevron-left",CHEVRON_RIGHT:"chevron-right",CHEVRON_UP:"chevron-up",CIRCLE_ARROW_REVERSE:"circle-arrow-reverse",CIRCLE_ARROW:"circle-arrow",CLOUD_DONE:"cloud-done",CLOUD_UPLOAD:"cloud-upload",CROSS:"cross",DOWNLOAD:"download",HOME:"home",MAGNIFIER:"magnifier",PERSON:"person",SKILL:"skill",SMILEY_HAPPY:"smiley_happy",SMILEY_HAPPY_SELECTED:"smiley_happy_selected",SMILEY_UNSURE:"smiley_unsure",SMILEY_UNSURE_SELECTED:"smiley_unsure_selected",SMILEY_VERY_HAPPY:"smiley_very_happy",SMILEY_VERY_HAPPY_SELECTED:"smiley_very_happy_selected",SMILEY_WORRIED:"smiley_worried",SMILEY_WORRIED_SELECTED:"smiley_worried_selected",THREE_DOTS:"three-dots"}},2056:function(e,t,r){"use strict";var n=r(446);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var a=n(r(2)),o=(0,n(r(451)).default)(a.default.createElement("path",{d:"M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm-2 14l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"}),"AssignmentTurnedIn");t.default=o},2057:function(e,t,r){"use strict";var n=r(446);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var a=n(r(2)),o=(0,n(r(451)).default)(a.default.createElement("path",{d:"M15.55 5.55L11 1v3.07C7.06 4.56 4 7.92 4 12s3.05 7.44 7 7.93v-2.02c-2.84-.48-5-2.94-5-5.91s2.16-5.43 5-5.91V10l4.55-4.45zM19.93 11c-.17-1.39-.72-2.73-1.62-3.89l-1.42 1.42c.54.75.88 1.6 1.02 2.47h2.02zM13 17.9v2.02c1.39-.17 2.74-.71 3.9-1.61l-1.44-1.44c-.75.54-1.59.89-2.46 1.03zm3.89-2.42l1.42 1.41c.9-1.16 1.45-2.5 1.62-3.89h-2.02c-.14.87-.48 1.72-1.02 2.48z"}),"RotateRight");t.default=o},2058:function(e,t,r){"use strict";var n=r(446);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var a=n(r(2)),o=(0,n(r(451)).default)(a.default.createElement("path",{d:"M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"}),"Done");t.default=o},2059:function(e,t,r){"use strict";var n=r(446);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var a=n(r(2)),o=(0,n(r(451)).default)(a.default.createElement("path",{d:"M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"}),"Clear");t.default=o},3200:function(e,t,r){"use strict";var n=r(445),a=r.n(n),o=r(2),c=r.n(o),s=r(6),i=r.n(s),l=r(2056),u=r.n(l),d=r(456),f=r(2059),p=r.n(f),E=r(2058),m=r.n(E),_=r(2057),v=r.n(_),b=r(798),S=r.n(b),g=r(1063),y=r.n(g),I=r(1382),O=r(3280),R=r(1048);function h(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter(function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable})),r.push.apply(r,n)}return r}function T(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?h(Object(r),!0).forEach(function(t){a()(e,t,r[t])}):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):h(Object(r)).forEach(function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))})}return e}var L=R.a.STATUS_AWAITING_REVIEW,w=R.a.STATUS_CAN_RETRY,A=R.a.STATUS_FAILED,M=R.a.STATUS_IN_PROGRESS,P=R.a.STATUS_NOT_STARTED,C=R.a.STATUS_PASSED,D=R.a.STATUS_READY_FOR_REVIEW,j={activityType:i.a.oneOf(["quiz","skill","project",""]),classes:i.a.objectOf(i.a.string),className:i.a.string,isBig:i.a.bool,isIconHidden:i.a.bool,number:i.a.number,status:i.a.string,forcedIcon:i.a.elementType},N={activityType:"",classes:{},className:"",isBig:!1,isIconHidden:!1,number:null,status:P,forcedIcon:null},H=function(e){var t,r,n,o=e.activityType,s=e.classes,i=e.className,l=e.status,d=e.number,f=e.isBig,E=e.isIconHidden,_=e.forcedIcon,b=(t={},a()(t,P,function(){return{skill:I.a.SKILL,project:y.a,quiz:u.a}[o]||null}),a()(t,M,function(){return v.a}),a()(t,L,function(){return S.a}),a()(t,C,function(){return m.a}),a()(t,w,function(){return I.a.CIRCLE_ARROW}),a()(t,A,function(){return p.a}),a()(t,D,function(){return I.a.ASSESSMENT}),t),g=(r={},a()(r,P,s.notStarted),a()(r,M,s.progress),a()(r,L,s.awaiting),a()(r,C,s.passed),a()(r,w,s.retry),a()(r,A,s.failed),a()(r,D,s.readyForReview),r),R={className:s.icon},h=_?function(){return _}:b[l];"function"!=typeof h&&(h=function(){return null});var T=h();"string"==typeof T?(n=O.a,R.name=T):n=T;var j=n&&!E?c.a.createElement(n,R):d,N=g[l]?g[l]:"",H=f?s.big:"";return c.a.createElement("div",{className:"".concat(s.root," ").concat(H," ").concat(N," ").concat(i)},j)};H.propTypes=j,H.defaultProps=N,t.a=Object(d.a)(function(e){var t=e.palette,r=e.spacing,n=e.typography;function a(e){return{color:e,borderColor:e}}function o(e){return{width:e,height:e,lineHeight:e}}var c={big:{container:r(5),smallIcon:".8em",normalIcon:"1em",bigIcon:"1.2em"},small:{container:r(3),smallIcon:".5em",normalIcon:".6em",bigIcon:".75em"}},s=function(e){return{"& $icon":o(e)}};return{root:T({},n.caption,{position:"relative",display:"flex",alignItems:"center",justifyContent:"center",borderRadius:"50%",textAlign:"center",flexShrink:0,boxSizing:"border-box !important",border:"1px solid"},o(c.small.container),{"&$notStarted":s(c.small.normalIcon),"&$passed":s(c.small.bigIcon),"&$failed":s(c.small.bigIcon),"&$awaiting":s(c.small.normalIcon),"&$retry":s(c.small.smallIcon),"&$progress":s(c.small.bigIcon),"&$readyForReview":s(c.small.bigIcon)}),big:T({},o(c.big.container),{"&$notStarted":s(c.big.normalIcon),"&$passed":s(c.big.bigIcon),"&$failed":s(c.big.bigIcon),"&$awaiting":s(c.big.normalIcon),"&$retry":s(c.big.smallIcon),"&$progress":s(c.big.bigIcon),"&$readyForReview":s(c.big.bigIcon)}),notStarted:a(t.status.notStarted),passed:T({},a(t.status.notStarted),{borderColor:t.status.success,background:t.status.success,color:"white"}),failed:a(t.status.fail),awaiting:a(t.status.awaiting),retry:a(t.status.retry),progress:a(t.status.inProgress),readyForReview:a(t.status.success),icon:{}}})(H)},798:function(e,t,r){"use strict";var n=r(446);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var a=n(r(2)),o=(0,n(r(451)).default)(a.default.createElement(a.default.Fragment,null,a.default.createElement("path",{d:"M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"}),a.default.createElement("path",{d:"M12.5 7H11v6l5.25 3.15.75-1.23-4.5-2.67z"})),"Schedule");t.default=o}}]);
//# sourceMappingURL=default~business~courseView~courses~dashboard~funnel~jobGuarantee~mcqView~mentorshipStudentDashboard~0c5d29d4.590f15059bac3874de53.js.map