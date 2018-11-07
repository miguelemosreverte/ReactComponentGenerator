import React from 'react';
import ReactDOM from 'react-dom';
import MiguelLemosStateless from './MiguelLemosStateless';

it('MiguelLemosStateless initial render', () => {
  const div = document.createElement('div');
  ReactDOM.render(<MiguelLemosStateless />, div);
  ReactDOM.unmountComponentAtNode(div);
});
