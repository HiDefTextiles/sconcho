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

#ifndef GRAPHICS_VIEW_H 
#define GRAPHICS_VIEW_H 

/* boost includes */
#include <boost/utility.hpp>

/* QT includes */
#include <QGraphicsView>
#include <QPointF>

/* local includes */

/* a few forward declarations */
class GraphicsScene;
class QMouseEvent;
class QRubberBand;

/* convenience typedefs */


/***************************************************************
 * 
 * The GraphicsView handles sconcho's main graphics interface
 * canvas 
 *
 ***************************************************************/
class PatternView
  :
  public QGraphicsView,
  public boost::noncopyable
{
  
  Q_OBJECT

    
public:

  explicit PatternView(GraphicsScene* scene, QWidget* myParent = 0);
  bool Init();

//signals:

//public slots:

protected:

  void mousePressEvent(QMouseEvent* evt);
  void mouseReleaseEvent(QMouseEvent* evt);
  void mouseMoveEvent(QMouseEvent* evt);
  
private:

  /* construction status variable */
  int status_;

  /* our canvas */
  GraphicsScene* canvas_;

  /* member variables */
  QRubberBand* rubberBand_;
  bool rubberBandOn_;
  QPoint rubberBandOrigin_;

  /* member functions */
  void initialize_rubberband_();
};


#endif
