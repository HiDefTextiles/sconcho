/***************************************************************
*
* (c) 2009-2010 Markus Dittrich
*
* This program is free software; you can redistribute it
* and/or modify it under the terms of the GNU General Public
* License Version 3 as published by the Free Software Foundation.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License Version 3 for more details.
*
* You should have received a copy of the GNU General Public
* License along with this program; if not, write to the Free
* Software Foundation, Inc., 59 Temple Place - Suite 330,
* Boston, MA 02111-1307, USA.
*
****************************************************************/

/* Qt headers */
#include <QDebug>


/* local headers */
#include "patternGridRectangle.h"


QT_BEGIN_NAMESPACE


/**************************************************************
 *
 * PUBLIC FUNCTIONS
 *
 **************************************************************/

//-------------------------------------------------------------
// constructor
//-------------------------------------------------------------
PatternGridRectangle::PatternGridRectangle( const QRectF& aPosition,
    QPen aPen, QGraphicsItem* aParent )
    :
    QGraphicsRectItem( aPosition, aParent ),
    currentPen_( aPen )
{
  status_ = SUCCESSFULLY_CONSTRUCTED;
}


//--------------------------------------------------------------
// main initialization routine
//--------------------------------------------------------------
bool PatternGridRectangle::Init()
{
  if ( status_ != SUCCESSFULLY_CONSTRUCTED ) {
    return false;
  }

  setPen( currentPen_ );

  return true;
}


//--------------------------------------------------------------
// return our custom object type
// so we can cast via
//--------------------------------------------------------------
int PatternGridRectangle::type() const
{
  return Type;
}


//-------------------------------------------------------------
// given a position inside our bounding box, returns true
// if the position is anywhere on the actual rectangle
// line (i.e. not the interior of the rectangle)
//-------------------------------------------------------------
bool PatternGridRectangle::selected( const QPointF& position )
const
{
  assert( boundingRect().contains( position ) );

  /* get rectangle covering only the inside (not the
   * actual rectangle line */
  QRectF inside( boundingRect() );
  qreal penWidth( currentPen_.widthF() );
  inside.adjust( penWidth, penWidth, -penWidth, -penWidth );

  return ( !inside.contains( position ) );
}


//-------------------------------------------------------------
// change our current pen
//-------------------------------------------------------------
void PatternGridRectangle::set_pen( QPen newPen )
{
  currentPen_ = newPen;
  setPen( currentPen_ );
}



/**************************************************************
 *
 * PUBLIC SLOTS
 *
 *************************************************************/



/**************************************************************
 *
 * PUBLIC MEMBER FUNCTIONS
 *
 *************************************************************/

/**************************************************************
 *
 * PROTECTED MEMBER FUNCTIONS
 *
 *************************************************************/

/**************************************************************
 *
 * PRIVATE SLOTS
 *
 *************************************************************/

/*************************************************************
 *
 * PRIVATE MEMBER FUNCTIONS
 *
 *************************************************************/

QT_END_NAMESPACE
