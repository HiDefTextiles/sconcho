/***************************************************************
*
* (c) 2009 Markus Dittrich 
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

#ifndef LEGEND_ITEM_H
#define LEGEND_ITEM_H

/* boost includes */
#include <boost/utility.hpp>

/* local includes */
#include "basicDefs.h"
#include "knittingPatternItem.h"



QT_BEGIN_NAMESPACE



/***************************************************************
 * 
 * a LegendItem is basically a KnittingPatternItem that is
 * a seperate type so we can pick it out from the canvas
 *
 ***************************************************************/
class LegendItem
  :
    public KnittingPatternItem
{
  
  Q_OBJECT

  
public:

  explicit LegendItem(const QSize& aDim, 
      int scale, const QColor& backColor = Qt::white,
      const QPoint& loc = QPoint(0,0));
  bool Init();

  /* return our object type; needed for qgraphicsitem_cast */
  enum { Type = UserType + LEGEND_ITEM_TYPE };
  int type() const;

private:

  /* some tracking variables */
  int status_;
};


QT_END_NAMESPACE

#endif