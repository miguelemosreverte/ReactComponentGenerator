import React from 'react';
import ReactDOM from 'react-dom';
import ReactTestClassNoprops from './ReactTestClassNoprops';

it('ReactTestClassNoprops initial render', () => {
  const div = document.createElement('div');
  ReactDOM.render(<ReactTestClassNoprops />, div);
  ReactDOM.unmountComponentAtNode(div);
});
