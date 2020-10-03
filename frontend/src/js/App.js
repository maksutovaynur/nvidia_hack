import React, {Fragment} from "react";
import {Tab, Tabs} from "@material-ui/core";
import {Link, Route, Switch} from "react-router-dom";
import '../style/app.sass';
import {SectionPeople} from "./components/SectionPeople";
import PeopleIcon from '@material-ui/icons/People';
import AppsIcon from '@material-ui/icons/Apps';
import WorkOutlineIcon from '@material-ui/icons/WorkOutline';
import EmojiObjectsIcon from '@material-ui/icons/EmojiObjects';


export const LayerTabs = [
    {
        title: "Main",
        path: "/",
        icon: (<AppsIcon/>)
    },
    {
        title: "People",
        path: "/people",
        icon: (<PeopleIcon/>),
        component: SectionPeople
    },
    {
        title: "Projects",
        path: "/projects",
        icon: (<WorkOutlineIcon/>)
    },
    {
        title: "Ideas",
        path: "/ideas",
        icon: (<EmojiObjectsIcon/>)
    },
];


export default function App() {
    return (
        <div className="app">
            <Route path="/" render={({location}) => (
                <Fragment>
                    <div className="app-header">
                        <Tabs value={location.pathname}>{
                            LayerTabs.map(
                                ({
                                     title,
                                     path,
                                     icon
                                }) => (
                                <Tab
                                    label={title}
                                    value={path}
                                    component={Link}
                                    to={path}
                                    icon={icon}
                                />
                            ))}
                        </Tabs>
                    </div>
                    <Switch>
                        {LayerTabs.map(({path, component}) => (
                            <Route exact path={path} component={component}/>
                        ))}
                    </Switch>
                </Fragment>
            )}/>
        </div>
    );
}
