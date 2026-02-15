"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[3857],{12088:function(e,t,i){i.d(t,{C:function(){return I},Z:function(){return _}});var a=i(52322),n=i(10081);i(2784);var r=i(46138),o=i(23906),s=i(52154),l=i(24062),d=i(19596),c=i(86704);let m=`
    position: absolute;
    left: 50%;
    user-select: none;
    max-height: 100%;
    max-width: 100%;

    /* hide left/right image affordance when not on a touch device */
    ${c.mediaQueries.devices.onCursorScreens} {
        &.peek { display: none; }
    }
`,u=`
    height: 100%;
    width: 100%;
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    left: 50%;
`,g=`
    top: 40%;
    transform: translate(-50%, -40%);
`,p=`
    top: 20%;
    transform: translate(-50%, -20%);
`,f=d.default.img.withConfig({componentId:"sc-b66608db-0"})([""," ",""],m,g),h=d.default.img.withConfig({componentId:"sc-b66608db-1"})([""," ",""],m,p),b=d.default.div.withConfig({componentId:"sc-b66608db-2"})([""," ",""],u,g),x=d.default.div.withConfig({componentId:"sc-b66608db-3"})([""," ",""],u,p),y=(0,n.ZP)`
    fragment MediaViewerImageMeta on Image {
        id
        url
        height
        width
        caption {
            plainText
        }
    }
`;function w(e,t){return e>t?{ImageElement:f,ContainerElement:b}:{ImageElement:h,ContainerElement:x}}let I=e=>{let{image:t,offset:i,prevImage:n,nextImage:d}=e,c=(0,r.Z)(),m=(0,o.wL)("MediaViewer_Image");if(!t||!t.url||!t.height||!t.width)return m.error("mediaviewer image missing required metadata",{id:t.id}),(0,a.jsx)(x,{className:"image-metadata-failure",children:(0,a.jsx)(l.F,{})});let u=w(t.height,t.width),g=u.ImageElement,p=u.ContainerElement,f=w(n?.height??0,n?.width??0),h=f.ImageElement,b=f.ContainerElement,y=w(d?.height??0,d?.width??0),I=y.ImageElement,_=y.ContainerElement,v=c.formatMessage({id:"mediaViewerImage_alt_missingCaption",defaultMessage:"Photo is missing caption."}),T=i||0;return(0,a.jsxs)(a.Fragment,{children:[!!n&&!!n.url&&(0,a.jsx)(b,{style:{maxHeight:`${n&&n.height||t.height}px`,maxWidth:`${n&&n.width||t.width}px`,left:`calc(-60% + ${T}px)`},children:(0,a.jsx)(h,{className:"peek",src:n.url,sizes:"100vw",srcSet:(0,s.gA)(n,!0),"data-image-id":`${n.id}-prev`,alt:n.caption?.plainText||v})}),(0,a.jsx)(p,{style:{maxHeight:`${t.height}px`,maxWidth:`${t.width}px`,left:`calc(50% + ${T}px)`},children:(0,a.jsx)(g,{src:t.url,sizes:"100vw",srcSet:(0,s.gA)(t,!0),"data-image-id":`${t.id}-curr`,alt:t.caption?.plainText||v})}),!!d&&!!d.url&&(0,a.jsx)(_,{style:{maxHeight:`${d&&d.height||t.height}px`,maxWidth:`${d&&d.width||t.width}px`,left:`calc(160% + ${T}px)`},children:(0,a.jsx)(I,{className:"peek",src:d.url,sizes:"100vw",srcSet:(0,s.gA)(d,!0),"data-image-id":`${d.id}-prev`,alt:d.caption?.plainText||v})})]})};I.fragments={image:y};var _=I},2791:function(e,t,i){i.d(t,{Se:function(){return _},ZP:function(){return v}});var a=i(52322),n=i(66898),r=i(97729),o=i.n(r);i(2784);var s=i(98042),l=i(75824),d=i(86958),c=i(49666),m=i(55634),u=i(8531),g=i(83163),p=i(48687),f=i(73183),h=i(54456),b=i(73286),x=i(52154),y=i(71225);let w=e=>{let{pageType:t,subPageType:i,pageConst:n}=e;return(0,a.jsxs)(a.Fragment,{children:[!!t&&(0,a.jsx)("meta",{property:"imdb:pageType",content:t}),!!i&&(0,a.jsx)("meta",{property:"imdb:subPageType",content:i}),!!n&&(0,a.jsx)("meta",{property:"imdb:pageConst",content:n})]})};var I=i(25436);let _=e=>{let t=(0,c.ik)(),i=(0,d.B)().context,{imageUrl:r,imageHeight:_,imageWidth:v}=function(){let e=arguments.length>0&&void 0!==arguments[0]&&arguments[0],t=arguments.length>1?arguments[1]:void 0,i=e?y.xJ:y.ax,a=e?y.Yv:y.Bs,n=e?y.Tm:y.yw;return t&&t.url&&t.width&&t.height&&(i=(0,x.y8)(t.url,y.sc),a=t.height/t.width*y.sc,n=y.sc),{imageUrl:i,imageHeight:a,imageWidth:n}}(t,e.image),T=(0,l.N)({id:"common_share_title",defaultMessage:"IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows"}),$=(0,l.N)({id:"common_share_description",defaultMessage:"IMDb is the world's most popular and authoritative source for movie, TV and celebrity content. Find ratings and reviews for the newest movie and TV shows. Get personalized recommendations, and learn where to watch across hundreds of streaming providers."}),C=(0,p.hg)({weblabID:g.lh.IMDB_NEXT_CLIENT_SIDE_NAVIGATION_323089,treatments:{T1:!0}}),M=e.title??T,j=e.description??$,E=e.openGraphData?.type||f.s.Website,S=i.sidecar?.localizationResponse?.isFullLocalizationEnabled,A=(S?i.sidecar?.localizationResponse?.languageForTranslations??"en_US":"en_US").replace("-","_"),L=function(e){let t=e.pageType,i=e.subPageType;return t===I.PageType.TITLE&&i===I.SubPageType.MAIN||t===I.PageType.NAME&&i===I.SubPageType.MAIN||t===I.PageType.VIDEO&&i===I.SubPageType.VIDEO_PLAYBACK_PAGE}(i),P=M,D=j;if(L){let t=e.openGraphData?.enhancedTitle;t&&t.length>0&&(P=t);let i=e.openGraphData?.enhancedDescription;i&&i.length>0&&(D=i)}let k="";if(e.noIndex||e.noFollow){let t=[];e.noIndex&&t.push("noindex"),e.noFollow&&t.push("nofollow"),e.noIndex&&!e.noFollow&&t.push("follow"),k=t.join(",")}return(0,a.jsxs)(o(),{children:[(0,u.n4)(m.yS.LOAD_META,C),(0,n.logCSAWidgetStart)(m.yS.LOAD_META,Date.now()),(0,a.jsx)("title",{children:M}),(0,a.jsx)("meta",{name:"description",content:j,"data-id":"main"},"page-desc"),!!e.keywords&&(0,a.jsx)("meta",{name:"keywords",content:e.keywords},"page-keywords"),(0,a.jsx)("meta",{name:"google-site-verification",content:"0cadf7898134e79b"}),(0,a.jsx)("meta",{name:"msvalidate.01",content:"C1DACEF2769068C0B0D2687C9E5105FA"}),!!k&&(0,a.jsx)("meta",{name:"robots",content:k}),!e.noIndex&&(0,a.jsx)("meta",{name:"robots",content:"max-image-preview:large"}),!!e.structuredData&&(0,a.jsx)("script",{...(0,s.h6)(e.structuredData)}),!!e.canonicalUrl&&(0,a.jsx)("meta",{property:"og:url",content:e.canonicalUrl},"fb_url"),(0,a.jsx)("meta",{property:"og:site_name",content:t?"IMDbPro":"IMDb"},"fb_site"),(0,a.jsx)("meta",{property:"og:title",content:P},"fb_title"),(0,a.jsx)("meta",{property:"og:description",content:D},"fb_desc"),(0,a.jsx)("meta",{property:"og:type",content:E},"fb_type"),(0,a.jsx)("meta",{property:"og:image",content:r},"fb_img"),(0,a.jsx)("meta",{property:"og:image:height",content:_.toString()},"fb_img_height"),(0,a.jsx)("meta",{property:"og:image:width",content:v.toString()},"fb_img_Width"),(0,a.jsx)("meta",{content:A,property:"og:locale"}),!!S&&!t&&function(e){let t=h.n.map(e=>e.replace("-","_"));return(0,a.jsx)(a.Fragment,{children:t.filter(t=>t!==e).map(e=>(0,a.jsx)("meta",{content:e,property:"og:locale:alternate"},`lc_alt_${e}`))})}(A),(0,a.jsx)("meta",{property:"twitter:site",content:t?"@IMDbPro":"@IMDb"},"tw_site"),(0,a.jsx)("meta",{property:"twitter:title",content:P},"tw_title"),(0,a.jsx)("meta",{property:"twitter:description",content:D},"tw_desc"),(0,a.jsx)("meta",{property:"twitter:card",content:"summary_large_image"},"tw_type"),(0,a.jsx)("meta",{property:"twitter:image",content:r},"tw_img"),(0,a.jsx)("meta",{property:"twitter:image:alt",content:j},"tw_img_alt"),!!e.canonicalUrl&&!e.noIndex&&(0,a.jsx)("link",{rel:"canonical",href:e.canonicalUrl}),(0,b.W)(e.hrefLangEntries),w(i),(0,u.vt)(m.yS.LOAD_META,C),(0,n.logCSAWidgetEnd)(m.yS.LOAD_META,Date.now()),(0,u.wx)(m.yS.LOAD_META,C),(0,n.logCSAWidgetLoad)(m.yS.LOAD_META,Date.now())]})};var v=_},71225:function(e,t,i){i.d(t,{Bs:function(){return r},Tm:function(){return l},Yv:function(){return d},ax:function(){return a},sc:function(){return o},xJ:function(){return s},yw:function(){return n}});let a="https://m.media-amazon.com/images/G/01/imdb/images/social/imdb_logo.png",n=1e3,r=1e3,o=1e3,s="https://m.media-amazon.com/images/S/sash/gje4y522toZQB1l.png",l=300,d=300},73183:function(e,t,i){var a,n;i.d(t,{s:function(){return a}}),(n=a||(a={})).MusicAlbum="music.album",n.MusicSong="music.song",n.Profile="profile",n.VideoEpisode="video.episode",n.VideoMovie="video.movie",n.VideoOther="video.other",n.VideoTvShow="video.tv_show",n.Website="website"},71954:function(e,t,i){i.d(t,{U:function(){return d}});var a=i(52322),n=i(88169),r=i(86704);i(2784);var o=i(19596);let s="confirmation-dialog-panel",l="confirmation-dialog-panel-content",d=e=>{let{isOpen:t,header:i,text:r,cancelLabel:o,confirmLabel:d,onCancel:f,onConfirm:h,className:b}=e;return(0,a.jsx)(c,{isOpen:t,baseColor:"base",panelClassName:s,contentClassName:l,className:b,children:(0,a.jsxs)(p,{children:[(0,a.jsx)(m,{"data-testid":"confirmation-dialog-header",children:i}),(0,a.jsx)(u,{"data-testid":"confirmation-dialog-text",children:r}),(0,a.jsxs)(g,{children:[!!o&&!!f&&(0,a.jsx)(n.SecondaryButton,{onClick:f,width:"full-width","data-testid":"confirmation-dialog-cancel",children:o}),(0,a.jsx)(n.Button,{onClick:h,width:"full-width","data-testid":"confirmation-dialog-confirm",children:d})]})]})})},c=(0,o.styled)(n.Dialog).withConfig({componentId:"sc-a8d43d73-0"})([".","{border-radius:1rem;overflow:hidden;}.","{display:flex;justify-content:center;}[class$='__backdrop']{backdrop-filter:blur(10px);}"],s,l),m=o.styled.div.withConfig({componentId:"sc-a8d43d73-1"})(["",""],(0,r.setTypographyType)("headline6")),u=o.styled.div.withConfig({componentId:"sc-a8d43d73-2"})(["",""],(0,r.setTypographyType)("body")),g=o.styled.div.withConfig({componentId:"sc-a8d43d73-3"})(["display:flex;gap:",";padding-top:",";"],r.spacing.xs,r.spacing.s),p=o.styled.div.withConfig({componentId:"sc-a8d43d73-4"})(["display:flex;flex-direction:column;gap:",";"],r.spacing.m);t.Z=d},1687:function(e,t,i){i.d(t,{V:function(){return eC}});var a=i(52322),n=i(88169),r=i(67353),o=i(72779),s=i.n(o),l=i(2784),d=i(75824),c=i(47069);function m(e){let{attributionUrl:t,text:i}=e,a=i||t;return t&&a?`<a href="${t}" target="_blank" rel="noopener nofollow">${a}</a>`:a?`${a}`:void 0}var u=i(10081),g=i(39366);let p={CLOSE:"media-sheet__close",OPEN:"media-sheet__open",EDIT:"media-sheet__edit",REPORT:"media-sheet__report"},f={PARENT:"media-sheet",ATTR_BANNER:"media-sheet__attr-banner",COUNT_DISPLAY:"media-sheet__count-display"},h=(0,u.ZP)`
    fragment MediaSheetImageMeta on Image {
        id
        type
        copyright
        createdBy
        caption {
            plaidHtml(queryParams: $queryParams)
        }
        titles {
            id
            titleText {
                text
            }
        }
        source {
            id
            attributionUrl
            text
            banner {
                url
                attributionUrl
            }
        }
        names {
            id
            nameText {
                text
            }
        }
        countries {
            text
        }
        languages {
            text
        }
        # On mobile, we need to refetch correctionLink and reportingLink
        # data with isInIframe: false.
        #
        # This refetching is handled by the ContributeActionButton component.
        correctionLink(
            relatedId: $id
            contributionContext: {
                isInIframe: true
                returnUrl: "${(0,g.Pj)()}"
                business: "consumer"
            }
        ) {
            url
        }
        reportingLink(
            relatedId: $id
            contributionContext: {
                isInIframe: true
                returnUrl: "${(0,g.Pj)()}"
                business: "consumer"
            }
        ) {
            url
        }
    }
`,b=(0,u.ZP)`
    fragment MediaSheetListItemMeta on ListItemNode {
        description {
            originalText {
                plaidHtml(queryParams: $queryParams)
            }
        }
    }
`,x={id:"common_buttons_close",defaultMessage:"Close"},y={id:"common_buttons_open",defaultMessage:"Open"},w={id:"mediaSheet_ariaLabel_edit",defaultMessage:"Edit tags"},I={id:"mediaSheet_ariaLabel_report",defaultMessage:"Report image"},_={id:"mediaSheet_label_name",defaultMessage:"People"},v={id:"mediaSheet_label_title",defaultMessage:"Titles"},T={id:"mediaSheet_label_country",defaultMessage:"Countries"},$={id:"mediaSheet_label_language",defaultMessage:"Languages"},C={id:"mediaSheet_attribution_photoBy",defaultMessage:"Photo by"},M={id:"mediaSheet_attribution_courtesy",defaultMessage:"Image courtesy"},j={id:"mediaSheet_ariaLabel_delete",defaultMessage:"Delete image"};var E=i(26806),S=i(41174),A=i(30634),L=i(11438),P=i(86704),D=i(19596);let k=(0,D.default)(n.IconButton).withConfig({componentId:"sc-a4f29a05-0"})(["","{margin-right:calc(var(--ipt-pageMargin) - 0.75rem);}"],P.mediaQueries.breakpoints.above.l);var N=e=>{let{name:t,label:i,className:n,isButton:r,onSelect:o,href:s}=e,l={name:t,label:i,className:n,onSelect:o,"data-testid":`mv-contrib-${t}`};return(0,a.jsx)(k,{...l,href:r?void 0:s})},R=e=>{let{actionName:t,className:i,flow:r,label:o,query:s}=e,l=(0,E.m8)(),d=(0,S.nu)(),{makeRefMarker:c}=(0,L.Lz)(),m=(0,n.useBreakpointsAsConfig)();if(!r)return null;let g=`${r.desktopLink}&ref_=${c(L.Cd.EDIT)}`,p=m.l||m.xl;return(0,a.jsx)(N,{name:t,label:o,className:i??"",onSelect:e=>{p?d?r.desktopOnOpen():(0,A.rf)(c(L.Cd.SIGN_IN)):(e.preventDefault(),l.query((0,u.ZP)`
                        query ContributeActionButton(
                            $imageId: ID!
                            $relatedId: ID!
                            $returnUrl: URL!
                        ) {
                            image(id: $imageId) {
                                correctionLink(
                                    relatedId: $relatedId
                                    contributionContext: {
                                        isInIframe: false
                                        returnUrl: $returnUrl
                                        business: "consumer"
                                    }
                                ) {
                                    url
                                }
                                reportingLink(
                                    relatedId: $relatedId
                                    contributionContext: {
                                        isInIframe: false
                                        returnUrl: $returnUrl
                                        business: "consumer"
                                    }
                                ) {
                                    url
                                }
                            }
                        }
                    `,{...s,returnUrl:window.location.href}).toPromise().then(e=>{let t=r.resolveMobileURL(e.data.image);window.open(t,"_self")}).catch(e=>{throw e}))},href:g,isButton:p})},V=i(46138),B=i(17503),O=i(71954);let U=(0,u.ZP)`
    mutation DeleteResumeImage($input: DeleteResumeImageInput!) {
        deleteResumeImage(input: $input) {
            success
            message {
                value
            }
        }
    }
`,Y={id:"mediaSheet_deleteImage_dialogHeader",defaultMessage:"Delete image?"},Q={id:"mediaSheet_deleteImage_dialogText",defaultMessage:"This will permanently remove the image from your profile."},F={id:"common_buttons_cancel",defaultMessage:"Cancel"},G={id:"common_buttons_delete",defaultMessage:"Delete"},Z={id:"common_buttons_close",defaultMessage:"Close"},W={id:"mediaSheet_deleteImage_successMessage",defaultMessage:"Your image has been deleted. Changes may take up to 24 hours to take effect."},q={id:"mediaSheet_delete_image_failureMessage",defaultMessage:"Something went wrong."},z={id:"mediaSheet_deleteImage_pendingDeleteHeaderText",defaultMessage:"Image deletion in progress"},H={id:"mediaSheet_deleteImage_pendingDeleteBodyText",defaultMessage:"This image is being removed from your profile. Changes may take up to one hour to complete."};var X=e=>{let{actionName:t,className:i,input:r,label:o}=e,s=(0,V.Z)(),d=(0,n.useBreakpointsAsConfig)(),{sendSnack:c}=(0,n.useSnackbar)(),[m,u]=l.useState(!1),[g,p]=l.useState(!1),[{data:f,error:h,fetching:b},x]=(0,B.Z)(U),y=s.formatMessage(W),w=s.formatMessage(q);l.useEffect(()=>{f?.deleteResumeImage.success?c({primaryText:y,type:"auto"}):(h||f?.deleteResumeImage.success===!1)&&(f?.deleteResumeImage.message?.value?.includes("No active image found")?p(!0):c({primaryText:w,type:"auto"}))},[f,h,y,w,c]);let I=d.l||d.xl;return(0,a.jsxs)(a.Fragment,{children:[(0,a.jsx)(N,{name:t,label:o,className:i??"",onSelect:e=>{e.preventDefault(),u(!0)},isButton:I}),(0,a.jsx)(O.Z,{isOpen:m,header:s.formatMessage(Y),text:s.formatMessage(Q),cancelLabel:s.formatMessage(F),confirmLabel:s.formatMessage(G),onCancel:()=>{u(!1)},onConfirm:()=>{u(!1),b||x({input:r})}}),(0,a.jsx)(O.Z,{isOpen:g,header:s.formatMessage(z),text:s.formatMessage(H),confirmLabel:s.formatMessage(Z),onConfirm:()=>{p(!1)}})]})};let K=D.default.div.withConfig({componentId:"sc-3d8c6ae9-0"})(["position:absolute;bottom:0;width:100%;max-height:calc(53% - 1.5rem);display:flex;z-index:2;","{max-height:calc(50%);}"],P.mediaQueries.devices.onTouchScreens),J=(0,D.default)(n.PageContentContainer).withConfig({componentId:"sc-3d8c6ae9-1"})(["position:relative;display:flex;width:100%;"]),ee=D.default.div.withConfig({componentId:"sc-3d8c6ae9-2"})([""," "," background:rgba(",",0.85);background:rgba(",",0.85);border-top:1px solid ",";border-top:1px solid ",";width:100%;display:flex;flex-direction:column;overflow:auto;transition:all 0.5s ease-out ","{height:100%;overflow:hidden;}"],(0,P.setTypographyType)("body"),(0,P.setPropertyToColorVar)("color","ipt-on-baseAlt-color"),(0,P.getColorVarValue)("ipt-baseAlt-shade3-rgb"),(0,P.getColorVar)("ipt-baseAlt-shade3-rgb"),(0,P.getColorVarValue)("ipt-baseAlt-border-color"),(0,P.getColorVar)("ipt-baseAlt-border-color"),P.mediaQueries.breakpoints.above.l),et=D.default.div.withConfig({componentId:"sc-3d8c6ae9-3"})([""," "," display:flex;justify-content:space-between;padding:0.5rem 1rem;padding:0.5rem ",";flex-shrink:0;"],(0,P.setTypographyType)("bodySmall"),(0,P.setPropertyToColorVar)("color","ipt-on-baseAlt-accent1-color"),(0,P.getSpacingVar)("ipt-pageMargin")),ei=D.default.span.withConfig({componentId:"sc-3d8c6ae9-4"})(["display:none;","{display:flex;}"],P.mediaQueries.breakpoints.only.m),ea=`
    position: relative;
    &::after {
        content: '';
        background: linear-gradient(
            to top,
            ${(0,P.getColorVarValue)("ipt-baseAlt-shade3-color")},
            transparent
        );
        background: linear-gradient(
            to top,
            ${(0,P.getColorVar)("ipt-baseAlt-shade3-color")},
            transparent
        );
        height: 1rem;
        width: 100%;
        position: absolute;
        bottom: 0;
        left: 0;
    }
`,en=D.default.div.withConfig({componentId:"sc-3d8c6ae9-5"})(["display:flex;flex-direction:column;","{height:100%;}"],P.mediaQueries.breakpoints.above.l),er=D.default.div.withConfig({componentId:"sc-3d8c6ae9-6"})(["display:flex;flex-direction:column;overflow:auto;flex-grow:2;","{flex-direction:row;overflow:hidden;","}"],P.mediaQueries.breakpoints.above.l,ea),eo=D.default.div.withConfig({componentId:"sc-3d8c6ae9-7"})(["width:100%;text-align:center;padding:0 1rem 0.5rem 1rem;padding:0 "," 0.5rem ",";","{","}"],(0,P.getSpacingVar)("ipt-pageMargin"),(0,P.getSpacingVar)("ipt-pageMargin"),P.mediaQueries.breakpoints.above.l,(0,P.setPropertyToColorVar)("background","ipt-baseAlt-shade3-bg")),es=(0,D.default)(n.HTMLContent).withConfig({componentId:"sc-3d8c6ae9-8"})(["padding:0 1rem 1rem;padding:0 "," 1rem;","{overflow:auto;flex-grow:1;width:60%;padding-right:1rem;height:100%;}"],(0,P.getSpacingVar)("ipt-pageMargin"),P.mediaQueries.breakpoints.above.l),el=D.default.div.withConfig({componentId:"sc-3d8c6ae9-9"})([""," margin:0 1rem;margin:0 ",";min-height:1px;min-width:1px;","{margin:0 0 1rem 0;}"],(0,P.setPropertyToColorVar)("background","ipt-baseAlt-border-color"),(0,P.getSpacingVar)("ipt-pageMargin"),P.mediaQueries.breakpoints.above.l),ed=D.default.div.withConfig({componentId:"sc-3d8c6ae9-10"})(["margin:0 1rem;margin:0 ",";padding-top:1rem;","{margin:0;padding:0 0.25rem 1rem 1rem;width:35%;overflow:auto;height:100%;}"],(0,P.getSpacingVar)("ipt-pageMargin"),P.mediaQueries.breakpoints.above.l),ec=D.default.div.withConfig({componentId:"sc-3d8c6ae9-11"})(["display:flex;justify-content:center;padding:0.5rem 0;","{margin-top:-0.5rem;justify-content:flex-start;flex-shrink:1;flex-direction:column;padding-top:0;}"],P.mediaQueries.breakpoints.above.l),em=`
    display: none;
    position: absolute;
    right: 4.5rem;
    ${P.mediaQueries.breakpoints.above.l} {
        display: block;
    }
`,eu=(0,D.default)(n.IconBorderButton).withConfig({componentId:"sc-3d8c6ae9-12"})([""," top:-1.125rem;z-index:1;transition:opacity 0.5s ease-in;opacity:",";visibility:",";"],em,e=>e.opacity,e=>e.visibility),eg=(0,D.default)(n.IconBorderButton).withConfig({componentId:"sc-3d8c6ae9-13"})([""," bottom:4rem;transition:opacity 0.5s ease-in;opacity:",";visibility:",";"],em,e=>e.opacity,e=>e.visibility),ep=D.default.div.withConfig({componentId:"sc-3d8c6ae9-14"})(["margin-bottom:0.25rem;",""],(0,P.setTypographyType)("bodySmall")),ef=D.default.span.withConfig({componentId:"sc-3d8c6ae9-15"})(["margin-right:0.5rem;font-weight:500;"]),eh=(0,D.default)(n.HTMLContent).withConfig({componentId:"sc-3d8c6ae9-16"})([""," ",""],(0,P.setPropertyToColorVar)("color","ipt-on-baseAlt-textSecondary-color"),(0,P.setTypographyType)("copyright")),eb=D.default.img.withConfig({componentId:"sc-3d8c6ae9-17"})(["max-width:100%;"]);var ex=i(66724),ey=i(87801);let ew=e=>{let{array:t,title:i}=e,{nameMainLinkBuilder:r,titleMainLinkBuilder:o}=(0,ex.WOb)(),s=[];for(let e=0;e<t.length;e++){let i=t[e];i.nameText?.text&&i.id?s.push((0,a.jsx)(n.TextLink,{href:r({nconst:i.id,refSuffix:ey.C.SEE_MORE}),text:i.nameText.text},`image-name-link-${i.id}`)):i.titleText?.text&&i.id?s.push((0,a.jsx)(n.TextLink,{href:o({tconst:i.id,refSuffix:ey.C.SEE_MORE}),text:i.titleText.text},`image-title-link-${i.id}`)):i.text&&s.push((0,a.jsx)("span",{children:i.text},`item-meta-${i.text}`)),e<t.length-1&&s.push(", ")}return(0,a.jsx)(a.Fragment,{children:s.length>0&&(0,a.jsxs)(ep,{children:[(0,a.jsx)(ef,{children:i}),(0,a.jsx)("span",{children:s})]})})};var eI=i(59904),e_=i(48687),ev=i(83163),eT=i(49996);let e$=(e,t)=>{(0,r.isEnterOrSpaceKey)(e)&&t()},eC=e=>{let{pageConst:t}=(0,eT.y)(),i=(0,eI.eS)(t??""),r=(0,e_.hg)({weblabID:ev.lh.IMDB_PRO_DELETE_IMAGE_1349297,treatments:{T1:!0}}),o={closeSheetAriaLabel:(0,d.N)(x),openSheetAriaLabel:(0,d.N)(y),editAriaLabel:(0,d.N)(w),reportAriaLabel:(0,d.N)(I),deleteAriaLabel:(0,d.N)(j),nameLabel:(0,d.N)(_),titleLabel:(0,d.N)(v),countryLabel:(0,d.N)(T),languageLabel:(0,d.N)($),photoByAttributionPrefix:(0,d.N)(C),courtesyAttributionPrefix:(0,d.N)(M)},{content:l,imageData:u,editFlow:g,reportFlow:h,isClosed:b,onCloseClicked:E,onOpenClicked:S}=e,A=b?0:1,L=b?"hidden":"visible",P=function(e,t){let{copyright:i,createdBy:a,source:n}=e;if(!i&&!a&&!n)return;let r=n&&m(n)?`${t.courtesyText} ${m(n)}`:void 0,o=[a?`${t.photoByText} ${a}`:void 0,i?`&copy;&nbsp;${i}`:void 0,r].filter(e=>!!e);return o.length?o.join(" - "):void 0}(u,{photoByText:o.photoByAttributionPrefix,courtesyText:o.courtesyAttributionPrefix}),D=()=>{u?.source?.text==="gettyimages.com"?(0,c.P)("offsite-gettyimages"):u?.source?.text==="mptvimages.com"&&(0,c.P)("offsite-mptvimages")};return(0,a.jsx)(K,{className:s()(e.className),children:(0,a.jsx)(n.SetPalette,{palette:"dark",children:(0,a.jsxs)(J,{children:[(0,a.jsx)(eg,{name:"info",className:p.OPEN,label:o.openSheetAriaLabel,onSelect:S,opacity:b?1:0,visibility:b?"visible":"hidden"}),(0,a.jsx)(eu,{label:o.closeSheetAriaLabel,className:p.CLOSE,name:"clear",onSelect:E,opacity:A,visibility:L}),(0,a.jsx)(ee,{"aria-hidden":b,style:{opacity:A,visibility:L},"data-testid":f.PARENT,children:(0,a.jsxs)(en,{children:[(0,a.jsxs)(et,{role:"presentation",children:[(0,a.jsx)("span",{children:l.contextTitle}),(0,a.jsx)(ei,{"data-testid":f.COUNT_DISPLAY,children:l.contextCount})]}),(0,a.jsxs)(er,{children:[(0,a.jsx)(es,{html:u.caption?.plaidHtml||""}),(0,a.jsx)(el,{}),(0,a.jsxs)(ed,{children:[!!u.names&&(0,a.jsx)(ew,{array:u.names,title:o.nameLabel}),!!u.titles&&(0,a.jsx)(ew,{array:u.titles,title:o.titleLabel}),!!u.countries&&(0,a.jsx)(ew,{array:u.countries,title:o.countryLabel}),!!u.languages&&(0,a.jsx)(ew,{array:u.languages,title:o.languageLabel}),!!P&&(0,a.jsx)("div",{onClick:D,onKeyDown:e=>{e$(e,D)},"data-testid":"copyright",children:(0,a.jsx)(eh,{html:P})})]}),(0,a.jsxs)(ec,{children:[(0,a.jsx)(R,{flow:g,actionName:"edit",label:o.editAriaLabel,className:p.EDIT,query:{imageId:e.imageData.id,relatedId:e.listId}}),"publicity"===u.type&&u.source?.id==="paidcustomer"&&i&&r?(0,a.jsx)(X,{actionName:"delete",label:o.deleteAriaLabel,className:p.REPORT,input:{id:u.id}}):(0,a.jsx)(R,{flow:h,label:o.reportAriaLabel,className:p.REPORT,actionName:"flag",query:{imageId:e.imageData.id,relatedId:e.listId}})]})]}),!!u.source?.banner&&(0,a.jsx)(eo,{"data-testid":f.ATTR_BANNER,children:(0,a.jsx)("a",{href:u.source.banner.attributionUrl,rel:"nofollow noopener noreferrer",target:"_blank",children:(0,a.jsx)(eb,{src:u.source.banner.url,height:u.source.banner.height,width:u.source.banner.width})})})]})})]})})})};eC.fragments={image:h,listItem:b}},9325:function(e,t,i){i.d(t,{$C:function(){return v},Ek:function(){return y},HP:function(){return b},KL:function(){return _},Qn:function(){return w},gG:function(){return h},k6:function(){return I},kH:function(){return x},s:function(){return p},ve:function(){return f},wO:function(){return T}});var a=i(10081),n=i(12088),r=i(1687),o=i(11438),s=i(85970);let l=(0,a.ZP)`
    fragment MediaViewerMeta on ImageConnection {
        pageInfo {
            endCursor
            hasNextPage
            hasPreviousPage
            startCursor
        }
        edges {
            position
            cursor
            node {
                ...MediaViewerImageMeta
                ...MediaSheetImageMeta
            }
        }
    }

    ${n.C.fragments.image}
    ${r.V.fragments.image}
`,d=(0,a.ZP)`
    fragment MediaViewerListMeta on ListConnection {
        pageInfo {
            endCursor
            hasNextPage
            hasPreviousPage
            startCursor
        }
        edges {
            position
            cursor
            node {
                item {
                    ...MediaViewerImageMeta
                    ...MediaSheetImageMeta
                }
                ...MediaSheetListItemMeta
            }
        }
    }
    ${n.C.fragments.image}
    ${r.V.fragments.image}
    ${r.V.fragments.listItem}
`,c=(0,a.ZP)`
    query NameImages(
        $id: ID!
        $before: ID
        $after: ID
        $jumpTo: ID
        $first: Int
        $last: Int
        $lastYes: Boolean!
        $firstYes: Boolean!
        $queryParams: String
    ) {
        name(id: $id) {
            nameText {
                text
            }
            meta {
                publicationStatus
            }
            images(first: $first, after: $after, jumpTo: $jumpTo)
                @include(if: $firstYes) {
                total
                ...MediaViewerMeta
            }
            wrapFront: images(last: $last, before: $before)
                @include(if: $lastYes) {
                total
                ...MediaViewerMeta
            }
            wrapBack: images(first: $first) @include(if: $firstYes) {
                total
                ...MediaViewerMeta
            }
        }
    }
    ${l}
`,m=(0,a.ZP)`
    query TitleImages(
        $id: ID!
        $before: ID
        $after: ID
        $jumpTo: ID
        $first: Int
        $last: Int
        $lastYes: Boolean!
        $firstYes: Boolean!
        $queryParams: String
    ) {
        title(id: $id) {
            titleText {
                text
            }
            meta {
                publicationStatus
            }
            releaseYear {
                year
            }
            images(first: $first, after: $after, jumpTo: $jumpTo)
                @include(if: $firstYes) {
                total
                ...MediaViewerMeta
            }
            wrapFront: images(last: $last, before: $before)
                @include(if: $lastYes) {
                total
                ...MediaViewerMeta
            }
            wrapBack: images(first: $first) @include(if: $firstYes) {
                total
                ...MediaViewerMeta
            }
        }
    }
    ${l}
`,u=(0,a.ZP)`
    query GalleryImages(
        $id: ID!
        $before: ID
        $after: ID
        $jumpTo: ID
        $first: Int
        $last: Int
        $lastYes: Boolean!
        $firstYes: Boolean!
        $queryParams: String
    ) {
        imageGallery(id: $id) {
            galleryText
            images(first: $first, after: $after, jumpTo: $jumpTo)
                @include(if: $firstYes) {
                total
                ...MediaViewerMeta
            }
            wrapFront: images(last: $last, before: $before)
                @include(if: $lastYes) {
                total
                ...MediaViewerMeta
            }
            wrapBack: images(first: $first) @include(if: $firstYes) {
                total
                ...MediaViewerMeta
            }
        }
    }
    ${l}
`,g=(0,a.ZP)`
    query ListImages(
        $id: ID!
        $before: ID
        $after: ID
        $jumpTo: ID
        $first: Int
        $last: Int
        $lastYes: Boolean!
        $firstYes: Boolean!
        $queryParams: String
    ) {
        list(id: $id) {
            name {
                originalText
            }
            items(first: $first, after: $after, jumpTo: $jumpTo)
                @include(if: $firstYes) {
                total
                ...MediaViewerListMeta
            }
            wrapFront: items(last: $last, before: $before)
                @include(if: $lastYes) {
                total
                ...MediaViewerListMeta
            }
            wrapBack: items(first: $first) @include(if: $firstYes) {
                total
                ...MediaViewerListMeta
            }
        }
    }
    ${d}
`,p=e=>{switch(e){case s.b.GALLERY:return u;case s.b.LIST:return g;case s.b.NAME:return c;case s.b.TITLE:return m;default:throw Error("Unknown MediaViewerType: "+e)}},f=3,h=6,b=3,x=20,y="vanity",w={title:"title",name:"name",gallery:"imageGallery",list:"list"},I={right:o.Cd.NEXT,left:o.Cd.PREVIOUS},_={countLabel:{id:"mediaViewer_galleryCount_label",defaultMessage:"{position} of {total}"},previousImageLabel:{id:"mediaSheet_ariaLabel_previousImage",defaultMessage:"Previous"},nextImageLabel:{id:"mediaSheet_ariaLabel_nextImage",defaultMessage:"Next"},closePromptLabel:{id:"common_ariaLabel_closePrompt",defaultMessage:"Close Prompt"}},v={PARENT:"media-viewer",ACTION_BAR:"media-viewer__action-bar",ACTION_BAR_GALLERY_COUNT:"action-bar__gallery-count",MEDIA_SHEET:"media-viewer__media-sheet",PAGE_RIGHT:"media-viewer__page-right",PAGE_LEFT:"media-viewer__page-left",LOADER:"media-viewer__loader",IMAGE:"media-viewer__image",TOUCH_HANDLER:"media-viewer__touch-handler",CONTRIBUTE_EDIT_DRAWER:"contribute-edit-drawer",CONTRIBUTE_EDIT_IFRAME:"contribute-edit-iframe",CONTRIBUTE_REPORT_DRAWER:"contribute-report-drawer",CONTRIBUTE_REPORT_IFRAME:"contribute-report-iframe",PAGER_VISIBLE:"ipc-pager--visible"},T="pager-aria-live-region"},49265:function(e,t,i){i.d(t,{Bc:function(){return x},C1:function(){return y},D5:function(){return h},GX:function(){return f},Ov:function(){return p},ed:function(){return u},f$:function(){return m},vI:function(){return w},zL:function(){return b},zb:function(){return c}});var a=i(19596),n=i(88169),r=i(86704),o=i(24062),s=i(9325);let l=()=>`
    top: calc(47% - 4vh);
    transform: translateY(-47%);
`,d=`
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translateX(-50%) translateY(-50%);
`,c=a.default.div.withConfig({componentId:"sc-1c12727-0"})(["overflow:hidden;position:relative;:focus{outline:0;}.",",.","{display:none;}","{height:calc(100vh - 5rem);.",",.","{display:block;}}height:calc(100vh - 7rem);"],s.$C.CONTRIBUTE_EDIT_DRAWER,s.$C.CONTRIBUTE_REPORT_DRAWER,r.mediaQueries.breakpoints.above.m,s.$C.CONTRIBUTE_EDIT_DRAWER,s.$C.CONTRIBUTE_REPORT_DRAWER),m=(0,a.default)(n.Pager).withConfig({componentId:"sc-1c12727-1"})(["","{left:0.25rem;}","{","}",""],r.mediaQueries.breakpoints.below.xs,r.mediaQueries.breakpoints.above.xs,(0,r.setPropertyToSpacingVar)("left","ipt-pageMargin"),l),u=(0,a.default)(n.Pager).withConfig({componentId:"sc-1c12727-2"})(["","{right:0.25rem;}","{","}",""],r.mediaQueries.breakpoints.below.xs,r.mediaQueries.breakpoints.above.xs,(0,r.setPropertyToSpacingVar)("right","ipt-pageMargin"),l),g=`
    position: absolute;
    top: 0;
    z-index: 1;
    left: 50%;
    transform: translateX(-50%);
`,p=a.default.div.withConfig({componentId:"sc-1c12727-3"})([""," height:'50px';width:'365px';"],g),f=a.default.div.withConfig({componentId:"sc-1c12727-4"})([""," height:100%;width:100%;","{overflow-x:auto;}"],g,r.mediaQueries.devices.onTouchScreens),h=a.default.div.withConfig({componentId:"sc-1c12727-5"})(["","{position:absolute;height:100%;width:120%;}","{display:none;}"],r.mediaQueries.devices.onTouchScreens,r.mediaQueries.devices.onCursorScreens),b=a.default.div.withConfig({componentId:"sc-1c12727-6"})(["",""],d),x=(0,a.default)(o.F).withConfig({componentId:"sc-1c12727-7"})(["&&{","}"],d),y=a.default.div.withConfig({componentId:"sc-1c12727-8"})(["@keyframes slide-in{0%{left:50%;}100%{left:50%;}}"," height:100%;width:100%;animation:slide-in 1s;left:",";display:flex;align-items:center;justify-content:center;z-index:1;","{z-index:0;}> div{width:100%;height:100%;}#interstitial_responsive_wrapper,#interstitial_wrapper{display:flex;width:100%;height:100%;flex-direction:column;justify-content:center;align-items:center;}#interstitialplaceholderPattern{display:none;}"],d,e=>`calc(50% + ${e.offset}px)`,r.mediaQueries.devices.onTouchScreens),w=a.default.span.withConfig({componentId:"sc-1c12727-9"})([""," vertical-align:middle;","{display:none;}","{margin-right:0.325rem;text-align:right;}"],(0,r.setPropertyToColorVar)("color","ipt-on-baseAlt-accent1-color"),r.mediaQueries.breakpoints.only.m,r.mediaQueries.breakpoints.above.m)},85970:function(e,t,i){var a,n;i.d(t,{b:function(){return a}}),(n=a||(a={})).TITLE="title",n.NAME="name",n.GALLERY="gallery",n.LIST="list"},54456:function(e,t,i){i.d(t,{O:function(){return n},n:function(){return a}});let a=["en-US","es-ES","es-MX","fr-FR","fr-CA","it-IT","pt-BR","hi-IN","de-DE"],n=e=>a.includes(e)},59904:function(e,t,i){i.d(t,{Oo:function(){return s},eS:function(){return n}});var a=i(86958);let n=e=>{let{context:t}=(0,a.B)();return r(t,e)},r=(e,t)=>o(e).includes(t),o=e=>e.sidecar?.account?.hasOwnershipOf||[],s=e=>{let{context:t}=(0,a.B)(),i=e??t.pageConst??"";return r(t,i)}}}]);